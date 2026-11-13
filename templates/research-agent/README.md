# Research Agent

An AI agent that searches the web with [Exa](https://exa.ai) and writes an answer with numbered sources. Good base for research assistants, fact checkers, news digests, scholarship or job finders, and any agent that needs fresh information from the web.

## How it works

1. You ask a question.
2. Exa searches the web and returns the most relevant pages.
3. The LLM writes a short answer using only those pages, and cites them as [1], [2]...

## Run it locally

```bash
cd templates/research-agent
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then add your LLM key and Exa key
uvicorn main:app --reload
```

Open http://localhost:8000.

## Make it yours

| Want to... | Change this |
| --- | --- |
| Search only certain sites (news, research papers) | The `json` body in `search_web()`. Exa supports filters like `includeDomains` and `category` |
| Change the answer style or length | The system prompt in `write_answer()` |
| Read more or fewer pages | `NUM_RESULTS` in `.env` |
| Add more steps (summarise, compare, email the result) | Add functions in `main.py` and call them in `research()` |

Exa docs: https://exa.ai/docs

## Deploy on Vultr

See [deploy/deploy-on-vultr.md](../../deploy/deploy-on-vultr.md). Use port `8000`.
