import streamlit as st
import requests
import json

# --- Load the FAQ Knowledge Base ---
def load_faq_knowledge_base(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    faq_dict = {}
    question = ""
    for line in lines:
        line = line.strip()
        if line.startswith("Q:"):
            question = line[3:].strip()
        elif line.startswith("A:") and question:
            answer = line[3:].strip()
            faq_dict[question] = answer
            question = ""
    return faq_dict

faq_knowledge_base = load_faq_knowledge_base("faq_knowledge_base.txt")

# --- FAQ Lookup Function ---
def get_faq_response(user_input):
    return faq_knowledge_base.get(user_input, None)

# --- Call NVIDIA LLaMA Model ---
def ask_llama(prompt):
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": "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",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta/llama3-70b-instruct",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 700
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except:
        return f"Unexpected response format: {response.text}"

# --- Streamlit App ---
st.set_page_config(page_title="ResoBridge AI Assistant", layout="centered")
st.title("🎓 ResoBridge Assistant")
st.markdown("**Ask me anything about your school. Dare me.**")

if "name" not in st.session_state:
    name_input = st.text_input("Hello, what do you want to call me?")
    if name_input:
        st.session_state.name = name_input
        st.success(f"Alright! You can call me {st.session_state.name}. Ask me anything.")
        st.stop()
else:
    st.markdown(f"✅ You’re now chatting with: **{st.session_state.name}**")

user_input = st.text_input("You:", "")

if user_input:
    faq_answer = get_faq_response(user_input)
    if faq_answer:
        st.write(f"**{st.session_state.name}:** {faq_answer}")
    else:
        ai_response = ask_llama(user_input)
        st.write(f"**{st.session_state.name}:** {ai_response}")
