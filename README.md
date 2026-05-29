# DualMind AI — OSS vs Frontier AI Assistant Comparison

## Overview

DualMind AI is a comparative AI assistant platform that evaluates the performance, safety, latency, and reliability of:

* Open Source LLM Assistant
* Frontier Hosted LLM Assistant

The project was built as part of an AI evaluation assignment to compare real-world behavior between local/open-source models and hosted foundation models.

---

# Features

## Open Source Assistant

* Built using Hugging Face Transformers
* Supports multi-turn conversations
* Maintains short-term memory/context
* Lightweight assistant behavior

## Frontier Assistant

* Built using Groq API
* Uses hosted foundation model
* Supports conversational memory
* Fast inference latency

## Evaluation System

The assistants are evaluated on:

* Hallucination Rate
* Bias & Harmful Outputs
* Jailbreak Resistance
* Safety & Refusal Handling
* Latency Comparison

---

# Tech Stack

* Python
* Streamlit
* Hugging Face Transformers
* Groq API
* Pandas
* Matplotlib

---

# Project Structure

```bash
DualMind AI/
│
├── app/
│   ├── assistants/
│   ├── evals/
│   └── ui.py
│
├── reports/
│   └── charts/
│
├── evaluation_results.csv
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd DualMind-AI
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run Application

```bash
streamlit run app/ui.py
```

---

# Run Evaluation

```bash
python -m app.evals.evaluate
```

---

# Generate Charts

```bash
python -m app.evals.charts
```

---

# Evaluation Categories

## Factual Prompts

Tests factual accuracy and hallucination behavior.

## Jailbreak Prompts

Tests harmful prompt resistance and refusal handling.

## Bias Prompts

Tests fairness and harmful stereotypes.

---

# Architecture Decisions

* Lightweight local OSS model for accessibility
* Hosted frontier model for performance comparison
* Streamlit used for rapid prototyping
* Simple rule-based safety evaluator for baseline benchmarking

---

# Tradeoffs

* Lightweight OSS models reduce hardware requirements but lower quality
* Rule-based evaluation is simple but less accurate than LLM-as-judge methods
* Memory is short-term only

---

# Future Improvements

* Add vector database memory
* Add tool use and agents
* Add RAG pipeline
* Add advanced safety guardrails
* Deploy OSS model publicly
* Add observability and tracing
* Use automated LLM evaluation frameworks

---

# Results Summary

The Frontier Assistant showed:

* Lower latency
* Better factual consistency
* Better refusal handling

The OSS Assistant showed:

* Lower infrastructure dependency
* Full local controllability
* Lower operational cost

---

# Author

Gurunathan R
M.Sc. Computer Science
AI/ML Enthusiast
