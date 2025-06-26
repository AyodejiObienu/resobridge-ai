# ai_engine.py
import requests
import pandas as pd

NVIDIA_API_KEY = "YOUR_NVIDIA_API_KEY"
MODEL_ID = "meta/llama3-70b-instruct"


def ask_llama(prompt):
    url = f"https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 800
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]


def generate_context_prompt(issues, school_status):
    issue_list = "\n".join([f"- {issue}" for issue in issues])
    status_context = f"""
Current School Resources:
- Plumbers: {school_status.get('plumbing_staff_available', 0)}
- Electricians: {school_status.get('electricians_available', 0)}
- Cleaning Teams: {school_status.get('cleaning_teams', 0)}
- Available Maintenance Budget: ₦{school_status.get('budget_remaining', 0)}
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
    return prompt


def run_analysis(csv_path, school_status):
    df = pd.read_csv(csv_path)
    batch_prompt = generate_context_prompt(df["issue_text"].tolist(), school_status)
    return ask_llama(batch_prompt)
