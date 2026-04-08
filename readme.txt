    - AI_powered_agent\dataset\bpss_agentic_dataset\evidence
    - AI_powered_agent\dataset\bpss_agentic_dataset\candidate_pack
    - AI_powered_agent\dataset\bpss_agentic_dataset\expected_outputs
    - AI_powered_agent\dataset\bpss_agentic_dataset\policies
    - AI_powered_agent\dataset\bpss_agentic_dataset\reference
    - AI_powered_agent\dataset\bpss_agentic_dataset\structured
    - AI_powered_agent\dataset\bpss_agentic_dataset\README.md

    - AI_powered_agent\readme.txt

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