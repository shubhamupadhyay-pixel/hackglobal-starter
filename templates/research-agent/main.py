"""HackGlobal starter: AI research agent (Exa web search + LLM answer with sources).

Flow: question -> Exa searches the web -> LLM writes an answer using only those sources.

Run locally:
    pip install -r requirements.txt
    cp .env.example .env   # then add your keys
    uvicorn main:app --reload
Open http://localhost:8000
"""
import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
EXA_API_KEY = os.getenv("EXA_API_KEY", "")
NUM_RESULTS = int(os.getenv("NUM_RESULTS", "5"))

app = FastAPI(title="HackGlobal Research Agent")


class ResearchRequest(BaseModel):
    question: str


def search_web(query: str) -> list[dict]:
    """Search the web with Exa and return title, url and a short text snippet per result."""
    resp = httpx.post(
        "https://api.exa.ai/search",
        headers={"x-api-key": EXA_API_KEY, "Content-Type": "application/json"},
        json={
            "query": query,
            "type": "auto",
            "numResults": NUM_RESULTS,
            "contents": {"highlights": True},
        },
        timeout=30,
    )
    resp.raise_for_status()
    sources = []
    for r in resp.json().get("results", []):
        snippet = " ".join(r.get("highlights") or []) or (r.get("text") or "")[:1000]
        sources.append({"title": r.get("title") or r.get("url"), "url": r.get("url"), "snippet": snippet})
    return sources


def write_answer(question: str, sources: list[dict]) -> str:
    """Ask the LLM to answer using only the sources, citing them as [1], [2]..."""
    context = "\n\n".join(
        f"[{i}] {s['title']} ({s['url']})\n{s['snippet']}" for i, s in enumerate(sources, start=1)
    )
    client = OpenAI(base_url=LLM_BASE_URL, api_key=LLM_API_KEY)
    result = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Answer the question using only the sources given. "
                "Cite sources inline like [1] or [2]. If the sources don't answer it, say so. "
                "Keep it under 200 words.",
            },
            {"role": "user", "content": f"Question: {question}\n\nSources:\n{context}"},
        ],
    )
    return result.choices[0].message.content


@app.get("/")
def home():
    return FileResponse(os.path.join(os.path.dirname(__file__), "static", "index.html"))


@app.get("/health")
def health():
    return {"status": "ok", "model": LLM_MODEL}


@app.post("/api/research")
def research(req: ResearchRequest):
    if not EXA_API_KEY:
        raise HTTPException(500, "EXA_API_KEY is not set. Add it to your .env file.")
    if not LLM_API_KEY:
        raise HTTPException(500, "LLM_API_KEY is not set. Add it to your .env file.")
    try:
        sources = search_web(req.question)
    except Exception as e:
        raise HTTPException(502, f"Exa search failed: {e}")
    if not sources:
        return {"answer": "No sources found for that question. Try rephrasing it.", "sources": []}
    try:
        answer = write_answer(req.question, sources)
    except Exception as e:
        raise HTTPException(502, f"LLM request failed: {e}")
    return {"answer": answer, "sources": [{"title": s["title"], "url": s["url"]} for s in sources]}
