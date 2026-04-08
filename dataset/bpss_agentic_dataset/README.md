# Compliance Intelligence Agent – BPSS Dataset

## Data Overview

This project implements an **agentic AI system** designed to analyze and reason over a **multi-format BPSS-style screening dataset**.

The goal is to simulate a real-world compliance workflow where information is distributed across:
- Structured data (CSV, XLSX)
- Unstructured documents (PDF, DOCX)
- Policy documents and reference materials

The system intelligently retrieves, combines, and reasons over this data to produce **evidence-backed answers**.

---

## Objective

The system is designed to:

1. Understand user queries  
2. Select appropriate tools (CSV search, vector search, policy checks)  
3. Retrieve relevant data from multiple sources  
4. Combine structured and unstructured evidence  
5. Detect inconsistencies, missing data, or compliance issues  
6. Provide **clear answers with supporting evidence**

---

## Core Capabilities

- Agent-based reasoning with tool selection  
- Multi-source data retrieval (CSV, PDF, DOCX, XLSX)  
- Semantic search using FAISS  
- Structured querying over tabular data  
- Evidence-backed answer generation  
- Detection of:
  - Missing documents  
  - Incomplete checks  
  - Conflicting information  
- Graceful handling of insufficient data  

---

## Dataset Description

The dataset represents a **fictional BPSS (Baseline Personnel Security Standard)** screening process.

It includes:

- Screening policies  
- Candidate documents (identity, employment, etc.)  
- Evidence logs (document inventory)  
- Structured trackers (CSV/XLSX)  
- Notes with potential inconsistencies or exceptions  

---

##  Example Questions You Can Ask

### Compliance & Status
- What are the compliance issues for candidate CAND-102?
- Which candidates are not ready for BPSS closure and why?
- Who has incomplete employment verification?

### Document & Evidence Checks
- What documents are missing for candidate CAND-105?
- Does candidate CAND-104 have valid identity proof?
- Show employment history for candidate CAND-102

### Policy & Violations
- Which records violate BPSS policies?
- Is employment gap allowed under policy?
- What does the policy say about identity verification?

### Cross-Source Reasoning
- Compare tracker status with document evidence for CAND-102
- Identify contradictions between notes and submitted documents
- Are there any risks flagged but not justified by evidence?

### Data Exploration
- What is in employment_history.csv?
- Show candidates with referee evidence
- List all candidates with missing address proof

---

## What This Demonstrates

This project showcases:

- Agentic AI system design  
- Multi-step reasoning over heterogeneous data  
- Integration of structured and unstructured sources  
- Real-world compliance and risk analysis workflows  
- Explainable AI outputs with traceable evidence  

---

## Success Criteria

A strong response from the system:

- Cites exact files and data sources  
- Distinguishes policy vs actual evidence  
- Identifies missing or inconsistent information  
- Avoids assumptions when data is incomplete  
- Provides structured, explainable answers  

---

## Notes

- This is a simulated dataset for demonstration purposes  
- Some records intentionally contain inconsistencies  
- The system is designed to detect and highlight such issues  

---

## How to Use

### 1. Build the vector index (mandatory first step)
```bash
python build_index_main.py
```

### Why this step is required?
- The system uses FAISS-based semantic search  
- FAISS requires a pre-built index  
- Without this step, the agent cannot retrieve document embeddings and will fail  

### 2. Run the agent
```bash
python main.py
```

### 3. Start asking questions in the terminal

---

## Author

Aakash Naralkar
