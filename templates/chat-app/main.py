"""HackGlobal starter: AI chat app (FastAPI backend + simple web page).

Run locally:
    pip install -r requirements.txt
    cp .env.example .env   # then add your keys
    uvicorn main:app --reload
Open http://localhost:8000
"""
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

# Works with any OpenAI-compatible provider (OpenAI, Vultr Serverless Inference, Groq, Ollama...).
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are a helpful assistant. Keep answers short and clear.",
)

app = FastAPI(title="HackGlobal Chat App")


class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/")
def home():
    return FileResponse(os.path.join(os.path.dirname(__file__), "static", "index.html"))


@app.get("/health")
def health():
    return {"status": "ok", "model": LLM_MODEL}


@app.post("/api/chat")
def chat(req: ChatRequest):
    if not LLM_API_KEY:
        raise HTTPException(500, "LLM_API_KEY is not set. Add it to your .env file.")
    client = OpenAI(base_url=LLM_BASE_URL, api_key=LLM_API_KEY)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += [m.model_dump() for m in req.messages[-20:]]  # keep the last 20 turns
    try:
        result = client.chat.completions.create(model=LLM_MODEL, messages=messages)
    except Exception as e:  # show the provider's error so it's easy to debug
        raise HTTPException(502, f"LLM request failed: {e}")
    return {"reply": result.choices[0].message.content}
