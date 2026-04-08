  Folder Structure

    - AI_powered_agent\dataset\bpss_agentic_dataset\evidence
    - AI_powered_agent\dataset\bpss_agentic_dataset\candidate_pack
    - AI_powered_agent\dataset\bpss_agentic_dataset\expected_outputs
    - AI_powered_agent\dataset\bpss_agentic_dataset\policies
    - AI_powered_agent\dataset\bpss_agentic_dataset\reference
    - AI_powered_agent\dataset\bpss_agentic_dataset\structured
    - AI_powered_agent\dataset\bpss_agentic_dataset\README.md

    - AI_powered_agent\readme.txt

    - AI_powered_agent\loaders\data_loader.py
    - AI_powered_agent\vector_store/build_index.py
    - AI_powered_agent\tools/vector_tool.py
    - AI_powered_agent\tools/csv_tool.pytools
    - AI_powered_agent\tools/policy_tool.py
    - AI_powered_agent\agent/agent.py
    - AI_powered_agent\main.py

evidence/ → supporting documents
candidate_pack/ → entity-specific data
policies/ → rules & compliance definitions
structured/ → CSV/Excel data
reference/ → extra context
expected_outputs/ → gold for evaluation

User Question
     ↓
Intent + Query Understanding (LLM)
     ↓
Agent decides:
   → Which tools to use
     ↓
TOOLS:
   1. Vector Search (PDF/Docs)
   2. Structured Query (CSV)
   3. Policy Checker
     ↓
Multi-source retrieval
     ↓
Reasoning + Synthesis
     ↓
Final Answer + Evidence

Python 3.11.9
pip 26.0.1 from C:\Users\AAKASH\AppData\Roaming\Python\Python314\site-packages\pip (python 3.14)
python -m venv ai_venv
ai_venv\Scripts\activate

pip install numpy pandas scikit-learn 
pip install langchain openai tiktoken
pip install faiss-cpu
pip install fastapi uvicorn python-dotenv
pip install sentence-transformers


Overall Plan
1. Load data
2. Create documents
3. Build vector store (FAISS)
4. Build tools
5. Build agent
6. Add reasoning + output formatting

⚠️ WARNINGS (NOT PROBLEMS)
1️⃣ LangChainDeprecationWarning
HuggingFaceEmbeddings is deprecated

👉 Safe to ignore for now ✅
👉 We’ll fix later when building agent

2️⃣ HF Token Warning
unauthenticated requests

👉 Not an error
👉 Just slower downloads

(Optional fix later)

3️⃣ BertModel UNEXPECTED

👉 Normal when loading embeddings
👉 Ignore ✅