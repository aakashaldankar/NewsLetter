# 📰 AI-Powered Newsletter Generator

Welcome to **NewsLetter**, an AI-driven project that automates the creation of insightful and well-designed newsletters using autonomous agents. With just a topic as input, the system handles everything—from research to content editing to newsletter formatting—all without human intervention.

HuggingFace Space Link: https://huggingface.co/spaces/aakashaldankar/NewsLetter

---

## 🚀 What is NewsLetter?

**NewsLetter** is a demonstration of how autonomous AI agents can work collaboratively to generate a complete newsletter. It combines the power of **CrewAI**, **LangChain**, **Groq LLM**, and the **EXA Web Search API** to handle:

1. 🕵️ **Research**
2. ✍️ **Editing**
3. 🎨 **Designing**

---

## 🤖 Meet the Agents

### 1. **Researcher**
- Utilizes the EXA web search tool.
- Searches for relevant articles and collects metadata.
- Gathers the most current and credible sources from the internet.

### 2. **Editor**
- Filters the research data.
- Summarizes content and ensures relevance.
- Follows a structured format and ensures readability.

### 3. **Designer**
- Converts the final content into HTML.
- Ensures all external links are functional.
- Produces a ready-to-use HTML newsletter.

---

## 🛠️ Tech Stack

| Component    | Technology              |
|--------------|--------------------------|
| Framework    | CrewAI                   |
| LLM          | LangChain + Groq LLM API |
| Web Search   | EXA Web Search Tool      |
| Interface    | Gradio                   |
| Language     | Python                   |

---

## 📁 Project Structure

```
NewsLetter/
│
├── config/
│   ├── agents.yaml
│   ├── newsletter_template.html
│   └── tasks.yaml
│
├── tools/
│   └── custom_tools.py
│
├── app.py
├── crew.py
├── requirements.txt
└── README.md
```

---

## 💻 How to Run Locally

### ✅ Prerequisites

- Python 3.10 or above
- Git
- A Groq API Key
- An EXA Web Search API Key

### 🧪 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/aakashaldankar/NewsLetter.git
cd NewsLetter
```

2. **Create and Activate a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

3. **Install the Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set Environment Variables**

Create a `.env` file in the root directory and add the following:

```
GROQ_API_KEY=your_groq_api_key
EXA_API_KEY=your_exa_api_key
```

5. **Run the Application**

```bash
python app.py
```

---

## 🌟 Why This Project Matters

**NewsLetter** is more than just an automation tool—it's a productivity revolution. This system:

- 🚀 Saves hours of manual work for marketers, journalists, and researchers.
- 📈 Ensures up-to-date content using real-time web search.
- 🎯 Delivers polished, publication-ready HTML newsletters.
- 💼 Can be customized for corporate, educational, and media organizations.

It combines the skills of a **researcher, editor, and developer**—all in one seamless AI workflow.

---

## 📮 Contact & Contribution

If you'd like to contribute or face any issues:

📧 Email: aakashaldankar@gmail.com  
🤝 Created by: **Aakash**

---

> “Let AI research, write, and design — you just provide the topic.” 🚀
