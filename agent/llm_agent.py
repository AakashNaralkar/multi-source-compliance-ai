# ==========================================
# 🔹 IMPORTS (FIXED)
# ==========================================
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent

import json

from tools.vector_tool import search_vector
from tools.csv_tool import search_csv, check_bpss_status
from tools.policy_tool import check_policy


# ==========================================
# 🔹 LLM SETUP
# ==========================================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# ==========================================
# 🔹 TOOLS
# ==========================================
@tool
def vector_search(query: str) -> str:
    return json.dumps(search_vector(query), indent=2)


@tool
def csv_search(query: str) -> str:
    return json.dumps(search_csv(query), indent=2)


@tool
def bpss_checker(query: str) -> str:
    return json.dumps(
        check_bpss_status(base_path="dataset/bpss_agentic_dataset/structured"),
        indent=2
    )


@tool
def policy_checker(query: str) -> str:
    return json.dumps(check_policy(query), indent=2)


tools = [
    vector_search,
    csv_search,
    bpss_checker,
    policy_checker
]


# ==========================================
# 🔹 SYSTEM PROMPT (REPLACES PromptTemplate)
# ==========================================
system_prompt = """
You are an enterprise AI agent.

- Use tools when needed
- You can use multiple tools
- Always give reasoning
- Always include evidence
- If unsure → say "insufficient data"
"""


# ==========================================
# 🔹 CREATE AGENT (FIXED)
# ==========================================
agent = create_agent(
    model=llm,              # ✅ FIXED
    tools=tools,
    system_prompt=system_prompt   # ✅ FIXED
)


# ==========================================
# 🔹 RUN
# ==========================================
def run_llm_agent(query):
    try:
        result = agent.invoke({
            "messages": [
                {"role": "user", "content": query}
            ]
        })

        return {
            "status": "success",
            "answer": result["messages"][-1].content
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }