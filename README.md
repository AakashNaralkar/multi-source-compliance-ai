# AI-Powered Compliance Agent

An intelligent multi-source AI agent designed to analyze compliance data, detect issues, and provide evidence-based answers by reasoning across structured and unstructured data.

---

## Overview

This project implements an **enterprise-style AI agent** capable of:

- Understanding user queries
- Selecting appropriate data sources
- Retrieving information from multiple formats (CSV, PDF, DOCX)
- Performing cross-document reasoning
- Providing **structured, evidence-backed answers**

---

## Key Features

- Multi-source data integration (structured + unstructured)  
- Semantic search using FAISS + embeddings  
- Rule-based + LLM-based reasoning  
- Modular tool-based architecture (LangChain)  
- BPSS compliance checking logic  
- Policy interpretation engine  
- Structured, explainable outputs  

---

## Architecture

The system is built using a **tool-augmented LLM agent**:

- **LLM**: Groq (LLaMA 3.3)
- **Vector Search**: FAISS + HuggingFace embeddings
- **Structured Data**: Pandas (CSV processing)
- **Agent Framework**: LangChain

---

## Setup Instructions

###  1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-source-compliance-ai.git
cd multi-source-compliance-ai
```

---

###  2. Python Version

Use:

Python 3.11.9

---

###  3. Create Virtual Environment

#### Windows (PowerShell)

```bash
python -m venv ai_venv
ai_venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv ai_venv
source ai_venv/bin/activate
```

---

###  4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

###  5. Set Environment Variables

Create a `.env` file in root:

```
GROQ_API_KEY=your_api_key_here
```

Do NOT commit `.env` to GitHub

---

###  6. Build Vector Index (MANDATORY FIRST STEP)

```bash
python build_index_main.py
```

### Why this step is required?

- The system uses **FAISS vector search** for unstructured data
- FAISS requires a pre-built index (`faiss_index/`)
- Without this step, the agent will crash because no index exists
- This step loads all documents and converts them into searchable embeddings

---

###  7. Run the Agent

```bash
python main.py
```

---

## Example Queries

- What are the compliance issues for a specific candidate?
- Which records violate BPSS policies?
- Identify missing documents for verification
- Summarize findings from reports and structured data

---

## How It Works

1. User submits a query  
2. Agent selects appropriate tools  
3. Tools retrieve data:
   - Vector search → documents  
   - CSV search → structured records  
   - BPSS checker → validation logic  
   - Policy checker → compliance rules  
4. Agent reasons across results  
5. Returns structured output:

```
Analysis:
...

Evidence:
...

Final Answer:
...
```

---

## Technologies Used

- LangChain  
- Groq LLM (LLaMA 3.3)  
- FAISS  
- HuggingFace Transformers  
- Pandas  
- Python 3.11.9  

---

## Author

Aakash N

---

## If you found this useful, consider giving it a star!
