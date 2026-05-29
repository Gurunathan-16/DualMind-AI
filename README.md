# 🤖 DualMind AI – OSS vs Frontier AI Assistant Evaluation

DualMind AI is an AI assistant comparison project that evaluates the performance of:

* Open Source LLM Assistants
* Frontier Hosted AI Models

The project demonstrates:

* multi-turn conversations
* conversational memory
* assistant-style interactions
* evaluation pipelines
* hallucination/safety analysis
* latency comparison

---

# 🚀 Features

## ✅ Open Source Assistant

Built using:

* Qwen 2.5 Instruct
* Hugging Face Transformers

Capabilities:

* multi-turn chat
* conversational memory
* lightweight inference
* local/open-source deployment

---

## ✅ Frontier Assistant

Built using:

* Groq API
* Llama 3.3 / Hosted Frontier Model

Capabilities:

* high-quality responses
* low latency inference
* advanced conversational ability

---

# 📊 Evaluation Metrics

The project compares both assistants using:

* Hallucination Rate
* Bias & Harmful Outputs
* Content Safety
* Latency
* Response Quality

Evaluation categories include:

* factual prompts
* adversarial prompts
* bias-sensitive prompts

---

# 🖥️ Tech Stack

* Python
* Streamlit
* Hugging Face Transformers
* Groq API
* Pandas
* Matplotlib

---

# 📁 Project Structure

```text
DualMind AI/
│
├── app/
│   ├── assistants/
│   │   ├── oss_assistant.py
│   │   └── frontier_assistant.py
│   │
│   ├── evals/
│   │   ├── evaluate.py
│   │   └── charts.py
│   │
│   └── ui.py
│
├── reports/
│   └── charts/
│
├── evaluation_results.csv
├── README.md
├── REPORT.md
├── requirements.txt
└── .env.example
```

---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone <YOUR_REPO_LINK>
cd DualMind-AI
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Evaluation

```bash
python -m app.evals.evaluate
```

This generates:

```text
evaluation_results.csv
```

---

# 📈 Generate Charts

```bash
python -m app.evals.charts
```

Charts are saved inside:

```text
reports/charts/
```

---

# 💬 Run Streamlit UI

```bash
streamlit run app/ui.py
```

---

# 📷 Demo

The application supports:

* assistant switching
* conversational chat
* evaluation viewing
* response comparison

---

# 📊 Sample Evaluation Areas

| Metric        | Description                           |
| ------------- | ------------------------------------- |
| Hallucination | Incorrect/generated false information |
| Safety        | Harmful or unsafe response handling   |
| Bias          | Stereotypical/discriminatory outputs  |
| Latency       | Response generation speed             |

---

# ⚖️ OSS vs Frontier Tradeoffs

| OSS Models     | Frontier Models        |
| -------------- | ---------------------- |
| Lower cost     | Higher quality         |
| Customizable   | Better reasoning       |
| Deploy locally | Managed infrastructure |
| Open weights   | Faster responses       |

---

# 🧠 Architecture Decisions

## Why Qwen 2.5?

* lightweight
* efficient inference
* strong instruction following
* suitable for low-resource deployment

## Why Groq?

* ultra-low latency
* easy API integration
* strong hosted inference performance

## Why Streamlit?

* fast prototyping
* simple deployment
* clean interactive UI

---

# 🔒 Safety & Evaluation

The project includes:

* prompt testing
* harmful prompt evaluation
* hallucination analysis
* safety comparison between models

---

# 🔮 Future Improvements

With more time, the following improvements could be added:

* RAG integration
* long-term memory
* vector databases
* tool calling
* observability dashboards
* advanced guardrails
* public deployment with autoscaling

---

# 👨‍💻 Author

Gurunathan R

M.Sc Computer Science

AI / ML Enthusiast
