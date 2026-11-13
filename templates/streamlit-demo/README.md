# Streamlit Demo

The fastest way to a working AI demo. Everything is in one Python file (`app.py`), with no HTML or JavaScript to write. Great for first-time builders, non-technical teammates and quick prototypes.

## Run it locally

```bash
cd templates/streamlit-demo
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then open .env and add your API key
streamlit run app.py
```

It opens at http://localhost:8501.

## Make it yours

- Change `SYSTEM_PROMPT` in `.env` to give the AI a job (tutor, career coach, recipe planner...).
- Add inputs like `st.file_uploader`, `st.selectbox` or `st.slider` in `app.py`.
- Streamlit docs: https://docs.streamlit.io

## Deploy on Vultr

See [deploy/deploy-on-vultr.md](../../deploy/deploy-on-vultr.md). Use port `8501`.
