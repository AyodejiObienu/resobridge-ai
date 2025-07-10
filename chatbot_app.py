import streamlit as st
import os
from ai_engine import ask_llama

st.set_page_config(page_title="ResoBridge Assistant", page_icon="🎓")
st.title("🎓 ResoBridge Assistant")
st.caption("Ask me anything about your school. Dare me.")

if "assistant_name" not in st.session_state:
    st.session_state.assistant_name = None

if st.session_state.assistant_name is None:
    name = st.text_input("Hello, what do you want to call me?")
    if name:
        st.session_state.assistant_name = name.strip()
        st.success(f"✅ You’re now chatting with: {st.session_state.assistant_name}")

if st.session_state.assistant_name:
    user_input = st.text_input("You:")

    blocked_keywords = ["politics", "religion", "insult"]
    if user_input:
        if any(word in user_input.lower() for word in blocked_keywords):
            st.warning("🚫 This topic is restricted. Please ask something else.")
        else:
            with open("Chatbot/faq_knowledge_base.txt", "r") as f:
                kb = f.read()
            context_prompt = f"""
Knowledge Base:
{kb}

Your name is {st.session_state.assistant_name}. Use the knowledge base above to answer questions.

User: {user_input}
"""
            response = ask_llama(context_prompt)
            st.markdown(f"**{st.session_state.assistant_name}:** {response}")
