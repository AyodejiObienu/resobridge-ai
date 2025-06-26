import streamlit as st
import pandas as pd
import requests
import json

# CONFIG
NVIDIA_API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
NVIDIA_API_KEY = "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"  # <- Replace with your key

# FAQ DATABASE
faq_data = {
    "how to submit a complaint": "Log in, go to 'Submit Issue', fill out the form, and hit submit.",
    "how to check complaint status": "Go to your dashboard and check the 'My Complaints' section.",
    "what is resobridge": "ResoBridge is an AI-enhanced platform that connects students with campus services."
}

# Session state
if "assistant_name" not in st.session_state:
    st.session_state.assistant_name = None

# UI layout
st.set_page_config(page_title="ResoBridge AI", layout="wide")
st.title("🤖 ResoBridge A.I. Intelligence & Chat Assistant")

st.sidebar.header("Choose Function")
mode = st.sidebar.radio("Select a mode", ["Intelligence Report", "Chatbot"])

