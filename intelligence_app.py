import streamlit as st
import pandas as pd
from ai_engine import ask_llama

st.set_page_config(page_title="ResoBridge Intelligence Layer", page_icon="🧠")
st.title("🧠 ResoBridge Intelligence Layer")
st.caption("Upload a CSV file with student complaints to analyze issues and receive data-informed suggestions.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded data:")
    st.dataframe(df)

    if st.button("Analyze Issues"):
        issues = df["issue_text"].tolist()
        school_status = {
            "plumbing_staff_available": 1,
            "electricians_available": 1,
            "cleaning_teams": 2,
            "budget_remaining": 25000,
        }

        issue_list = "\n".join([f"- {issue}" for issue in issues])
        status_context = f"""
Current School Resources:
- Plumbers: {school_status['plumbing_staff_available']}
- Electricians: {school_status['electricians_available']}
- Cleaning Teams: {school_status['cleaning_teams']}
- Available Maintenance Budget: ₦{school_status['budget_remaining']}
"""

        prompt = f"""
You are an internal AI advisor for university operations. Analyze these student complaints:

{issue_list}

{status_context}

Only suggest realistic, actionable steps based on the school's capacity.
Return a structured, professional report with:
- Categorization
- Trends or patterns
- Suggested actions (based on available resources)
- Preventive measures
"""

        result = ask_llama(prompt)
        st.subheader("🧠 ResoBridge A.I. Intelligence Report")
        st.markdown(result)
