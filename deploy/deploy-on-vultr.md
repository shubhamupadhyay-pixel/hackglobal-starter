# Deploy on Vultr

This guide puts your app live on the internet with a Vultr Cloud Compute server and Docker. It takes about 15 minutes and works for every template in this repo.

**Before you start:** claim your $200 Vultr credits (see the HackGlobal Hacker Guide). The smallest server plan is enough for a hackathon demo.

## 1. Create a server

1. Log in to the [Vultr Console](https://my.vultr.com) and click **Deploy** (or **Deploy +**), then **Deploy New Server**.
2. Choose **Cloud Compute** (Shared CPU).
3. Pick a location close to you or your users.
4. For the image, choose **Ubuntu** (latest LTS).
5. Pick the smallest plan with at least 1 GB RAM.
6. Give it a name (for example `hackglobal-yourteam`) and click **Deploy Now**.

Wait a minute or two until the status shows **Running**. On the server's **Overview** page, note the **IP Address**, **Username** (root) and **Password**.

## 2. Connect to the server

On Mac or Linux, open Terminal. On Windows, open PowerShell.

```bash
ssh root@YOUR_SERVER_IP
```

Type `yes` when asked, then paste the password from the Overview page (it won't show as you type).

## 3. Install Docker and Git

```bash
curl -fsSL https://get.docker.com | sh
apt-get install -y git
```

## 4. Get your code on the server

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO/templates/chat-app      # or the folder your app is in
```

Create your `.env` file on the server (it is not in GitHub, which is correct):

```bash
cp .env.example .env
nano .env
```

Add your real keys, then press `Ctrl+O`, `Enter`, `Ctrl+X` to save and exit.

## 5. Build and run your app

For **chat-app** or **research-agent** (port 8000):

```bash
docker build -t myapp .
docker run -d --name myapp --restart unless-stopped --env-file .env -p 80:8000 myapp
```

For **streamlit-demo** (port 8501):

```bash
docker build -t myapp .
docker run -d --name myapp --restart unless-stopped --env-file .env -p 80:8501 myapp
```

## 6. Open the firewall

```bash
ufw allow 80/tcp
```

If it says `ufw: command not found` or `Firewall not enabled`, that's fine. Skip this step.

## 7. Check it's live

Open `http://YOUR_SERVER_IP` in your browser. This is your **Live Demo URL** for the submission.

## Updating your app

After you push new code to GitHub:

```bash
cd ~/YOUR_REPO && git pull
cd templates/chat-app                # your app folder
docker rm -f myapp
docker build -t myapp .
docker run -d --name myapp --restart unless-stopped --env-file .env -p 80:8000 myapp
```

## Something not working?

| Problem | Try this |
| --- | --- |
| Page doesn't load | Run `docker ps`. If your app isn't listed, run `docker logs myapp` to see the error |
| "LLM_API_KEY is not set" | Check your `.env` file on the server, then rerun step 5 |
| Port already in use | Run `docker rm -f myapp`, then rerun step 5 |
| Still stuck | Ask in the HackGlobal 2026 Discord server with a screenshot of the error |

## Optional: Vultr Serverless Inference

Vultr also offers an OpenAI-compatible LLM API. To use it with these templates, set this in `.env`:

```
LLM_BASE_URL=https://api.vultrinference.com/v1
LLM_API_KEY=your-vultr-inference-key
LLM_MODEL=a-model-from-your-vultr-inference-dashboard
```

Check the Vultr Console for availability, pricing and the model list before you rely on it. Docs: https://docs.vultr.com/how-to-use-vultr-cloud-inference-in-python

## When the hackathon ends

Your credits cover the event. Keep your server running until judging is done. After that, add a payment method to keep it live, or destroy the server to stop usage.
