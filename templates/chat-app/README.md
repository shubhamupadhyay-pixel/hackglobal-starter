# Chat App

A simple AI chat app: a Python (FastAPI) backend that talks to an LLM, and a one-page web UI. Good base for assistants, tutors, support bots or any "ask AI" product.

## Run it locally

```bash
cd templates/chat-app
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then open .env and add your API key
uvicorn main:app --reload
```

Open http://localhost:8000 and start chatting.

## Make it yours

| Want to... | Change this |
| --- | --- |
| Change how the AI behaves | `SYSTEM_PROMPT` in `.env` |
| Use a different model or provider | `LLM_BASE_URL`, `LLM_MODEL` in `.env` |
| Change the look | `static/index.html` |
| Add new features or API routes | `main.py` |

## Deploy on Vultr

See [deploy/deploy-on-vultr.md](../../deploy/deploy-on-vultr.md). Use port `8000`.
