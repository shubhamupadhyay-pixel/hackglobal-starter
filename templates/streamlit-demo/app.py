"""HackGlobal starter: quick AI demo in Streamlit (pure Python, no frontend code).

Run locally:
    pip install -r requirements.txt
    cp .env.example .env   # then add your key
    streamlit run app.py
"""
import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are a helpful assistant. Keep answers short and clear.",
)

st.set_page_config(page_title="HackGlobal AI Demo", page_icon="💡")
st.title("HackGlobal AI Demo")
st.caption("Edit app.py to turn this into your own product.")

if not LLM_API_KEY:
    st.error("LLM_API_KEY is not set. Add it to your .env file and restart.")
    st.stop()

client = OpenAI(base_url=LLM_BASE_URL, api_key=LLM_API_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages[-20:],
                stream=True,
            )
            reply = st.write_stream(
                chunk.choices[0].delta.content or ""
                for chunk in stream
                if chunk.choices
            )
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"LLM request failed: {e}")
