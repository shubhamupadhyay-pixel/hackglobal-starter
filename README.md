# HackGlobal 2026 Starter Kit

Ready-to-use templates to help you start building in minutes at **HackGlobal 2026**, a global hackathon by Polaris School of Technology, co-powered by Vultr.

You can build in any language or stack. These templates are optional, just a fast way to start.

## Pick a template

| Template | Best for | Stack | Port |
| --- | --- | --- | --- |
| [chat-app](templates/chat-app) | AI assistants, tutors, support bots | Python (FastAPI) + HTML | 8000 |
| [research-agent](templates/research-agent) | Agents that search the web and answer with sources | Python (FastAPI) + Exa + HTML | 8000 |
| [streamlit-demo](templates/streamlit-demo) | Fast prototypes, first-time builders, non-technical teams | Python (Streamlit) | 8501 |

All templates work with any OpenAI-compatible LLM provider (OpenAI, Vultr Serverless Inference, Groq, Ollama and more). You only change three lines in `.env`.

## Get started in 4 steps

1. Click **Use this template** (top right) to make your own copy of this repo. Keep it **public** so judges can see it.
2. Clone your copy and open the template folder you want.
3. Follow that folder's README to run it locally.
4. Deploy it on Vultr with [deploy/deploy-on-vultr.md](deploy/deploy-on-vultr.md).

Delete the templates you don't use, and replace this README with your own using [docs/project-readme-template.md](docs/project-readme-template.md).

## What's inside

```
hackglobal-starter/
├── templates/
│   ├── chat-app/          AI chat app (FastAPI + web page)
│   ├── research-agent/    Web search agent (Exa + LLM)
│   └── streamlit-demo/    Quick AI demo in pure Python
├── deploy/
│   └── deploy-on-vultr.md Step-by-step deploy guide
└── docs/
    ├── project-readme-template.md
    └── submission-checklist.md
```

## Before you submit

Go through [docs/submission-checklist.md](docs/submission-checklist.md). Submissions happen on Vultr Community, and late submissions are not accepted.

## Need help?

Ask in the HackGlobal 2026 Discord server. Mentors and organizers are there throughout the hackathon.

## Keep your keys safe

Never commit your `.env` file or paste API keys in your code. The `.gitignore` in this repo already blocks `.env`.
