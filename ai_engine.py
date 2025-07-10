import requests
import pandas as pd

import streamlit as st
import os

MODEL_ID = "meta/llama3-70b-instruct"
NVIDIA_API_KEY = st.secrets["NVIDIA_API_KEY"]

def ask_llama(prompt):
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.4,
        "max_tokens": 800
    }
    response = requests.post(url, headers=headers, json=data)
    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return f"⚠️ Unexpected response format: {response.json()}"
