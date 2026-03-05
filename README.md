# 🌉 ResoBridge AI Platform

> **Bridging the Gap Between Student Concerns and Institutional Solutions**

ResoBridge AI is an intelligent platform designed to streamline student issue management in educational institutions. It combines conversational AI with data-driven intelligence to handle FAQs, resolve common student queries, and provide actionable insights to administrators.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Technical Stack](#technical-stack)
- [Configuration](#configuration)
- [Contributing](#contributing)

---

## 🎯 Overview

ResoBridge AI addresses the critical challenge of student support systems in educational institutions by providing two integrated modules:

1. **🎓 Chatbot Module** - Handles frequently asked questions and provides instant, personalized responses
2. **🧠 Intelligence Layer** - Analyzes student complaints and generates actionable recommendations based on institutional capacity

The platform leverages the Meta Llama 3 70B model via NVIDIA's API to deliver intelligent, context-aware responses while maintaining institutional constraints and resource awareness.

---

## 🔴 Problem Statement

### The Challenge

Educational institutions face several critical challenges in student support:

1. **Information Overload**: Students constantly ask similar questions about admission policies, tuition, facilities, academic requirements, etc. Manual responses are time-consuming and inconsistent.

2. **Inefficient Issue Resolution**: Student complaints are submitted through various channels and often go unanswered or take too long to resolve, leading to student dissatisfaction.

3. **Lack of Data-Driven Decision Making**: Administrators have difficulty identifying patterns in student issues to prioritize maintenance, resource allocation, and policy improvements.

4. **Resource Constraints**: Institutions have limited staff, budgets, and resources but must maintain high-quality student support. There's no systematic way to match available resources to student needs.

5. **Scalability Issues**: As student populations grow, manual support systems become increasingly ineffective and costly.

### Why ResoBridge AI?

ResoBridge AI solves these problems by:

- **Automating FAQ Responses**: Instantly answering common questions 24/7 using AI
- **Intelligent Issue Analysis**: Automatically categorizing and analyzing student complaints to identify trends
- **Resource-Aware Recommendations**: Suggesting realistic solutions based on actual institutional capacity
- **Data-Driven Insights**: Providing actionable intelligence to support decision-making
- **Scalable Support**: Handling unlimited concurrent student queries without additional staffing

---

## ✨ Features

### 🎓 Chatbot Module Features
- **Conversational Interface**: Natural language Q&A about school policies and procedures
- **Knowledge Base Integration**: Draws from comprehensive FAQ knowledge base
- **Personalization**: Students can customize the assistant's name for engaging interaction
- **Content Filtering**: Built-in safeguards against inappropriate topics (politics, religion, insults)
- **Context-Aware Responses**: Uses institutional knowledge base to provide accurate answers
- **Session Management**: Maintains conversation state for smooth user experience

### 🧠 Intelligence Layer Features
- **CSV File Upload**: Bulk import of student issues for analysis
- **Issue Categorization**: Automatically groups complaints by type
- **Trend Analysis**: Identifies patterns and recurring problems
- **Resource Awareness**: Considers available staff, equipment, and budget
- **Actionable Recommendations**: Suggests realistic next steps based on capacity
- **Professional Reporting**: Generates structured, executive-ready reports
- **Preventive Measures**: Recommends proactive solutions to reduce future issues

---

## 📁 Project Structure

```
resobridge-ai/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── ai_engine.py                       # Core AI engine (LLM wrapper)
├── chatbot_app.py                     # Chatbot Streamlit application
├── intelligence_app.py                # Intelligence Layer Streamlit application
├── faq_knowledge_base.txt             # Knowledge base for chatbot
│
├── Chatbot/                           # Chatbot module directory
│   └── faq_knowledge_base.txt         # FAQs and school information
│
├── student_issues.csv                 # Sample student issue data
├── issue_logs.csv                     # Historical issue logs
│
└── .devcontainer/                     # Dev container configuration
    └── (Development environment setup)
```

### File Descriptions

| File | Purpose |
|------|---------|
| `ai_engine.py` | Core module containing the `ask_llama()` function that communicates with NVIDIA's Llama API |
| `chatbot_app.py` | Streamlit-based chatbot UI for student queries |
| `intelligence_app.py` | Streamlit-based intelligence layer for issue analysis |
| `faq_knowledge_base.txt` | Comprehensive knowledge base with FAQs, policies, and institutional information |
| `requirements.txt` | Python package dependencies |
| `student_issues.csv` | Sample data for testing the intelligence layer |
| `issue_logs.csv` | Historical records of analyzed issues |

---

## 🏗️ Architecture

### System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    ResoBridge AI Platform                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────┐      ┌──────────────────────┐    │
│  │   🎓 Chatbot Module  │      │ 🧠 Intelligence Layer│    │
│  ├──────────────────────┤      ├──────────────────────┤    │
│  │ • User Input         │      │ • CSV File Upload    │    │
│  │ • FAQ Lookup         │      │ • Issue Extraction   │    │
│  │ • Content Filtering  │      │ • Trend Analysis     │    │
│  │ • Response Gen.      │      │ • Resource Matching  │    │
│  │                      │      │ • Recommendations    │    │
│  └──────────────────────┘      └──────────────────────┘    │
│           │                              ��                  │
│           └──────────────┬───────────────┘                  │
│                          │                                  │
│           ┌──────────────▼───────────────┐                 │
│           │   AI Engine (ai_engine.py)   │                 │
│           ├───────────────────────────────┤                 │
│           │ • NVIDIA Llama 3 70B API     │                 │
│           │ • Request Formatting         │                 │
│           │ • Response Parsing           │                 │
│           │ • Error Handling             │                 │
│           └───────────────────────────────┘                 │
│                          │                                  │
│           ┌──────────────▼───────────────┐                 │
│           │   NVIDIA API Endpoint        │                 │
│           │ https://integrate.api.nvidia │                 │
│           │  .com/v1/chat/completions   │                 │
│           └───────────────────────────────┘                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

```
┌─────────────┐
│   Student   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│  Choose Module                      │
├──────────────────┬──────────────────┤
│  Chatbot (FAQ)   │  Intelligence    │
└────────┬─────────┴──────┬───────────┘
         │                │
         ▼                ▼
   ┌──────────────┐  ┌──────────────┐
   │ Query Input  │  │ Upload CSV   │
   └──────┬───────┘  └──────┬───────┘
          │                 │
          ▼                 ▼
   ┌──────────────┐  ┌──────────────┐
   │Filter Check  │  │Parse Data    │
   │(Safe Topics) │  │             │
   └──────┬───────┘  └──────┬───────┘
          │                 │
          ▼                 ▼
   ┌──────────────┐  ┌──────────────┐
   │Knowledge Base│  │Create Prompt │
   │+ Query       │  │with Resources│
   └──────┬───────┘  └──────┬───────┘
          │                 │
          └────────┬────────┘
                   │
                   ▼
           ┌──────────────────┐
           │ ai_engine.py     │
           │ ask_llama()      │
           └────────┬─────────┘
                    │
                    ▼
           ┌──────────────────┐
           │NVIDIA Llama API  │
           │Processing        │
           └────────┬─────────┘
                    │
                    ▼
           ┌──────────────────┐
           │Response Generated│
           └────────┬─────────┘
                    │
                    ▼
           ┌──────────────────┐
           │Display to User   │
           │ (Markdown Format)│
           └──────────────────┘
```

---

## 💻 Technical Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend/UI** | Streamlit | Interactive web interface for both modules |
| **AI/LLM** | Meta Llama 3 70B (via NVIDIA API) | Core language model for understanding and generation |
| **Data Processing** | Pandas | CSV handling and data manipulation |
| **HTTP Requests** | Requests | API communication with NVIDIA endpoints |
| **Runtime** | Python 3.8+ | Language runtime |
| **Deployment** | Streamlit Cloud | Easy deployment and hosting |

---

## 📊 Component Details

### 1. **ai_engine.py** - The AI Core

```
┌────────────────────────────────┐
│      ai_engine.py              │
├────────────────────────────────┤
│ Configuration:                 │
│ • Model: meta/llama3-70b-inst  │
│ • API Key: From st.secrets     │
│ • Temperature: 0.4             │
│ • Max Tokens: 800              │
│                                │
│ Function: ask_llama(prompt)    │
│ ├─ Format request              │
│ ├─ Add authentication          │
│ ├─ Call NVIDIA API             │
│ ├─ Parse response              │
│ └─ Return text or error        │
└───────────────────────��────────┘
```

**Key Function**: `ask_llama(prompt)`
- Takes any prompt string
- Calls NVIDIA's Llama API with proper authentication
- Returns the model's response or error message
- Temperature set to 0.4 for factual accuracy

### 2. **chatbot_app.py** - Student FAQ Assistant

```
┌────────────────────────────────┐
│    chatbot_app.py              │
├────────────────────────────────┤
│ UI: 🎓 ResoBridge Assistant    │
│                                │
│ 1. Get Assistant Name          │
│    └─ Personalize experience   │
│                                │
│ 2. Load FAQ Knowledge Base     │
│    └─ Read Chatbot/*.txt       │
│                                │
│ 3. Filter Input                │
│    └─ Block: politics,         │
│       religion, insults        │
│                                │
│ 4. Build Context Prompt        │
│    ├─ Knowledge Base           │
│    ├─ Assistant Name           │
│    └─ Student Question         │
│                                │
│ 5. Call AI Engine              │
��    └─ Get Response             │
│                                │
│ 6. Display Result              │
│    └─ Markdown formatted       │
└────────────────────────────────┘
```

**Workflow**:
1. User names the chatbot assistant
2. Student asks a question
3. Content filter checks for inappropriate topics
4. FAQ knowledge base is combined with the question
5. Llama model generates contextual response
6. Answer displayed with assistant's name

### 3. **intelligence_app.py** - Issue Analysis Engine

```
┌────────────────────────────────┐
│   intelligence_app.py          │
├────────────────────────────────┤
│ UI: 🧠 Intelligence Layer      │
│                                │
│ 1. Upload CSV File             │
│    └─ Extract issues           │
│                                │
│ 2. Define Resources            │
│    ├─ Plumbing staff: 1        │
│    ├─ Electricians: 1          │
│    ├─ Cleaning teams: 2        │
│    └─ Budget: ₦25,000          │
│                                │
│ 3. Create Analysis Prompt      │
│    ├─ Issue list               │
│    ├─ Resource context         │
│    └─ Request structure        │
│                                │
│ 4. Call AI Engine              │
│    └─ Analyze with constraints │
│                                │
│ 5. Generate Report             │
│    ├─ Categorization           │
│    ├─ Trends                   │
│    ├─ Actions (realistic)      │
│    └─ Prevention measures      │
└────────────────────────────────┘
```

**Key Features**:
- Accepts CSV with `issue_text` column
- Considers actual institutional resources
- Generates structured reports with:
  - Issue categorization
  - Pattern identification
  - Resource-constrained recommendations
  - Preventive strategies

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- NVIDIA API Key (from NVIDIA's developer portal)
- Streamlit account (for deployment, optional)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/AyodejiObienu/resobridge-ai.git
cd resobridge-ai
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up NVIDIA API Key**
   - Get your API key from NVIDIA's developer portal
   - For local development, create a `.streamlit/secrets.toml` file:
   ```toml
   NVIDIA_API_KEY = "your-api-key-here"
   ```

5. **Run the application**
```bash
# Run Chatbot
streamlit run chatbot_app.py

# Run Intelligence Layer (in another terminal)
streamlit run intelligence_app.py
```

---

## 📖 Usage Guide

### Chatbot Module

```
1. Open the Chatbot application
2. Enter a name for your AI assistant (e.g., "Alex", "StudyBuddy")
3. Ask any question about school policies, procedures, facilities
4. Get instant, knowledge-base-backed responses
5. Continue the conversation naturally

Example Questions:
- "What are the admission requirements?"
- "How much is the tuition fee?"
- "What facilities are available in the library?"
- "How do I register for courses?"
```

### Intelligence Layer Module

```
1. Prepare a CSV file with columns: issue_text
   Example:
   ┌─────────────────────────────────────────┐
   │ issue_text                              │
   ├─────────────────────────────────────────┤
   │ Broken toilet in Block A                │
   │ Electrical outlet not working           │
   │ Ceiling leaking in dormitory C          │
   │ Broken doors on stadium changing room   │
   │ Dirty corridors in administration block │
   └─────────────────────────────────────────┘

2. Upload the CSV file to the Intelligence Layer
3. Click "Analyze Issues"
4. Review the generated report with:
   - Issue categorization
   - Identified trends
   - Prioritized actions
   - Preventive recommendations
```

---

## 🔧 Configuration

### Model Parameters (in ai_engine.py)

```python
MODEL_ID = "meta/llama3-70b-instruct"  # AI model
Temperature = 0.4                       # Lower = more factual
Max_tokens = 800                        # Response length limit
```

**Why these settings?**
- **Temperature 0.4**: Keeps responses factual and consistent (not creative/random)
- **Max tokens 800**: Ensures concise, readable responses
- **Llama 3 70B**: Balance of capability and API availability

### Resource Settings (in intelligence_app.py)

```python
school_status = {
    "plumbing_staff_available": 1,
    "electricians_available": 1,
    "cleaning_teams": 2,
    "budget_remaining": 25000,  # ₦25,000
}
```

**Customize these** to match your institution's actual resources!

### Content Filters (in chatbot_app.py)

```python
blocked_keywords = ["politics", "religion", "insult"]
```

**Modify** to add/remove inappropriate topics as needed.

---

## 📋 Sample Data Files

### student_issues.csv
```csv
issue_text
Broken toilet in Block A
Electrical outlet not working in lab
Ceiling leaking in dormitory
Broken chairs in lecture hall
Dirty corridors need cleaning
```

### issue_logs.csv
```csv
date,category,status
2026-03-01,Plumbing,Resolved
2026-03-02,Electrical,Pending
2026-03-03,Cleaning,Resolved
```

---

## 🎨 User Interface

### Chatbot Interface
```
┌─────────────────────────────���───────────┐
│  🎓 ResoBridge Assistant                │
│  Ask me anything about your school.     │
│  Dare me.                               │
├─────────────────────────────────────────┤
│                                         │
│  Hello, what do you want to call me?   │
│  [_____________________] Enter         │
│                                         │
│  ✅ You're now chatting with: StudyBot │
│                                         │
│  You: [_____________________]          │
│                                         │
│  StudyBot: The tuition fees are ₦250k  │
│  per semester...                        │
│                                         │
└─────────────────────────────────────────┘
```

### Intelligence Layer Interface
```
┌─────────────────────────────────────────┐
│  🧠 ResoBridge Intelligence Layer       │
│  Upload a CSV file with student         │
│  complaints to analyze issues...        ���
├─────────────────────────────────────────┤
│                                         │
│  Upload CSV [Browse...] ✓              │
│                                         │
│  📄 Uploaded data:                      │
│  ┌─────────────────────────────────┐   │
│  │ issue_text                      │   │
│  ├─────────────────────────────────┤   │
│  │ Broken toilet in Block A         │   │
│  │ Electrical outlet not working    │   │
│  │ Ceiling leaking in dormitory     │   │
│  └─────────────────────────────────┘   │
│                                         │
│  [Analyze Issues]                      │
│                                         │
│  🧠 ResoBridge A.I. Intelligence Report│
│  ### Issue Categorization              │
│  - Plumbing: 1 issue                   │
│  - Electrical: 1 issue                 │
│  ...                                    │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🔐 Security Considerations

1. **API Key Protection**
   - Never commit API keys to version control
   - Use Streamlit secrets or environment variables
   - Rotate keys regularly

2. **Content Filtering**
   - Filter inappropriate topics in chatbot
   - Log all interactions for audit trail

3. **Data Privacy**
   - Handle student data according to regulations
   - Don't store sensitive information in logs

4. **Rate Limiting**
   - NVIDIA API has rate limits
   - Monitor usage to avoid quota breaches

---

## 🚧 Limitations & Future Improvements

### Current Limitations
- Single knowledge base for all students
- Fixed resource definitions
- No user authentication
- No persistent conversation history
- Limited to text input/output

### Planned Improvements
- Multi-language support
- Student profile customization
- Admin dashboard for resource management
- Integration with student management systems
- Mobile app version
- Real-time notification system
- Machine learning for resource optimization

---

## 📞 Support & Contact

For issues, questions, or contributions:
- **GitHub Issues**: [https://github.com/AyodejiObienu/resobridge-ai/issues](https://github.com/AyodejiObienu/resobridge-ai/issues)
- **Author**: Ayodeji Obienu
- **Email**: Contact via GitHub profile

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🙏 Acknowledgments

- NVIDIA for the Llama 3 API access
- Streamlit for the web framework
- Meta for the Llama 3 model
- Educational institutions for the inspiration

---

**Last Updated**: March 5, 2026
**Version**: 1.0.0
**Status**: Active Development
