# HackGlobal 2026 Starter Kit

**Free ready-made AI app templates, plus a step-by-step guide to go live on Vultr, so you can start building your idea in minutes.**

Made for **HackGlobal 2026**, a global hackathon by Polaris School of Technology, co-powered by Vultr.

## What is this?

This is a ready-made project you can copy, so you don't start from a blank screen. Instead of spending your first few hours on setup, you copy this, add your own idea and start building.

**Using it is optional.** You can build in any language or tool you like.

## What's inside

### 1. Three ready-to-use apps (pick one)

| App | What it is | Example ideas you could build |
| --- | --- | --- |
| [**Chat app**](templates/chat-app) | A website with a chat box where you talk to an AI, like a mini ChatGPT | Study tutor, career coach, customer support bot |
| [**Research agent**](templates/research-agent) | You ask a question, it searches the internet (using Exa) and gives a short answer with source links | Scholarship finder, news summariser, fact checker |
| [**Streamlit demo**](templates/streamlit-demo) | The simplest one: a basic AI chat built from a single Python file | Quick prototypes, beginners, non-technical teams |

Each app already works. You just add your AI key, run it, and then change it to fit your idea.

### 2. A "how to go live" guide

[**Deploy on Vultr**](deploy/deploy-on-vultr.md) shows you, step by step, how to put your app on a Vultr server so it gets a real web link anyone can open. Judges need this link to try your project, and it's also how you use your $200 Vultr credits.

### 3. Two helper documents

- [**Project description template**](docs/project-readme-template.md): a fill-in-the-blanks page to explain your project clearly (problem, solution, how it works, team). It makes your project easier for judges to understand.
- [**Submission checklist**](docs/submission-checklist.md): every field on the Vultr Community submission form, plus the common mistakes to avoid (private code, broken link, forgetting to select HackGlobal 2026).

## How to use it (4 steps)

1. **Copy it.** Click the green **Use this template** button at the top of this page, then **Create a new repository**. Keep it **Public** so judges can see your code.
2. **Pick one app.** Open its folder, follow the short README inside to run it on your laptop, and change it to fit your idea. Delete the apps you don't use.
3. **Put it live.** Follow [Deploy on Vultr](deploy/deploy-on-vultr.md) to get your web link.
4. **Submit.** Use the [submission checklist](docs/submission-checklist.md) and submit on Vultr Community before your region's close time. Late submissions are not accepted.

## What you'll need

- **An AI key.** The apps work with any OpenAI-compatible AI service (OpenAI, Vultr Serverless Inference, Groq and others). You paste the key into a settings file called `.env`. Each app's README shows how.
- **An Exa key**, only for the Research agent. HackGlobal participants get $20 in free Exa credits (link on Discord).
- **Python** installed on your laptop, if you want to run the app locally first.

## Need help?

Ask in the **HackGlobal 2026 Discord server**. Mentors and organizers are there throughout the hackathon.

## Keep your keys safe

Never put your API keys in your code or upload your `.env` file to GitHub. This repo is already set up to keep `.env` out of GitHub for you.

---

<details>
<summary><b>For developers: folder structure and tech details</b></summary>

```
hackglobal-starter/
├── templates/
│   ├── chat-app/          AI chat app (Python FastAPI + web page), port 8000
│   ├── research-agent/    Web search agent (Exa + LLM, FastAPI + web page), port 8000
│   └── streamlit-demo/    Quick AI demo in pure Python (Streamlit), port 8501
├── deploy/
│   └── deploy-on-vultr.md Deploy with Docker on Vultr Cloud Compute
└── docs/
    ├── project-readme-template.md
    └── submission-checklist.md
```

- Every template reads `LLM_BASE_URL`, `LLM_API_KEY` and `LLM_MODEL` from `.env`, so you can switch AI providers by changing three lines.
- Every template has a `Dockerfile`, a `requirements.txt` and an `.env.example`.
- Licensed under MIT. Use, change and share freely.

</details>
