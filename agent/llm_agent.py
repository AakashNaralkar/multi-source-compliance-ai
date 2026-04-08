from dotenv import load_dotenv
import os
import json

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent

from tools.vector_tool import search_vector
from tools.csv_tool import search_csv, check_bpss_status
from tools.policy_tool import check_policy



# LLM SETUP
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)



# TOOLS
@tool
def vector_search(query: str) -> str:
    """Search unstructured documents such as PDFs, DOCX files, and reports using semantic vector search."""
    return json.dumps(search_vector(query), indent=2)


@tool
def csv_search(query: str) -> str:
    """Search structured CSV data like candidate records, document inventory, and employment history."""
    return json.dumps(search_csv(query), indent=2)


@tool
def bpss_checker(query: str) -> str:
    """Check BPSS verification status and identify missing or incomplete checks required for closure."""
    results = check_bpss_status(base_path="dataset/bpss_agentic_dataset/structured")

    # Optional improvement: filter by query if provided
    if query:
        filtered = [r for r in results if query.lower() in str(r).lower()]
        return json.dumps(filtered if filtered else results, indent=2)

    return json.dumps(results, indent=2)


@tool
def policy_checker(query: str) -> str:
    """Check compliance policies and determine whether a requirement is mandatory, optional, or not required."""
    return json.dumps(check_policy(query), indent=2)


tools = [
    vector_search,
    csv_search,
    bpss_checker,
    policy_checker
]



# SYSTEM PROMPT
system_prompt = """
You are an enterprise-grade AI agent designed for compliance and investigation tasks.

Your job is to answer user questions by reasoning across multiple data sources.

Follow this STRICT process:

1. Understand the question
   - Identify the goal (compliance check, missing data, summary, violations)

2. Plan your approach
   - Decide which tools to use:
     • vector_search → unstructured data
     • csv_search → structured data
     • bpss_checker → BPSS status
     • policy_checker → compliance rules

3. Execute tool calls
   - You may use multiple tools
   - Combine results across sources

4. Reason over the results
   - Correlate information
   - Identify missing data or violations

5. Output MUST follow this format:

----------------------------------------
Analysis:
- Step-by-step reasoning
- Mention tools used

Evidence:
- Key findings from tools
- Include file names / sources

Final Answer:
- Clear, concise answer
----------------------------------------

Rules:
- NEVER hallucinate
- ALWAYS use tools when data is required
- If insufficient data → say "insufficient data"
- Be accurate and concise
"""

# AGENT
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)

def run_llm_agent(query):
    try:
        result = agent.invoke({
            "messages": [
                {"role": "user", "content": query}
            ]
        })

        # safer extraction
        if "messages" in result and len(result["messages"]) > 0:
            return result["messages"][-1].content

        return "Error: No response generated"

    except Exception as e:
        return f"Error: {str(e)}"