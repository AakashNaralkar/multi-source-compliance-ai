from tools.vector_tool import search_vector
from tools.csv_tool import search_csv, check_bpss_status
from tools.policy_tool import check_policy


def run_agent(query):
    query_lower = query.lower()

    print("\n🧠 Agent thinking...\n")

    # ==========================================
    # 🔥 TOOL SELECTION (SMART ROUTING)
    # ==========================================

    # 🔥 1. BPSS LOGIC (HIGHEST PRIORITY)
    if any(word in query_lower for word in ["bpss", "closure", "ready", "not ready", "verification", "screening"]):
        tool = "bpss_logic"
        print("👉 Using BPSS LOGIC ENGINE")

        # ✅ FIX: Explicit path (prevents weird reload issues)
        results = check_bpss_status(base_path="dataset/bpss_agentic_dataset/structured")

    # 🔹 2. POLICY QUESTIONS
    elif any(word in query_lower for word in ["policy", "required", "mandatory", "allowed"]):
        tool = "policy"
        print("👉 Using POLICY TOOL")
        results = check_policy(query)

    # 🔹 3. STRUCTURED DATA
    elif any(word in query_lower for word in ["candidate", "file", "record", "data"]):
        tool = "csv"
        print("👉 Using CSV TOOL")
        results = search_csv(query)

    # 🔹 4. DEFAULT → VECTOR SEARCH
    else:
        tool = "vector"
        print("👉 Using VECTOR SEARCH")
        results = search_vector(query)

    # ==========================================
    # 🔥 POST-PROCESSING (INTELLIGENCE LAYER)
    # ==========================================

    if isinstance(results, list) and len(results) > 0:

        # ==========================================
        # 🔥 BPSS OUTPUT (FIXED)
        # ==========================================
        if tool == "bpss_logic":

            # ✅ Handle "all clear" case
            if isinstance(results[0], str):
                return {
                    "analysis": "BPSS Closure Readiness",
                    "status": results[0]
                }

            return {
                "analysis": "BPSS Closure Readiness",
                "total_flagged": len(results),
                "candidates": results
            }

        # ==========================================
        # 🔹 POLICY OUTPUT
        # ==========================================
        elif tool == "policy":
            decisions = [r.get("decision") for r in results if isinstance(r, dict)]

            if "❌ Not Required" in decisions:
                final = "❌ Overall: NOT REQUIRED"
            elif "✅ Required" in decisions:
                final = "✅ Overall: REQUIRED"
            else:
                final = "⚠️ UNCLEAR — CHECK POLICY"

            return {
                "final_decision": final,
                "evidence": results
            }

        # ==========================================
        # 🔹 CSV OUTPUT
        # ==========================================
        elif tool == "csv":
            if isinstance(results[0], str):
                return {"answer": "No structured data found"}

            return {
                "answer": "Structured data retrieved",
                "records_found": len(results),
                "data": results
            }

        # ==========================================
        # 🔹 VECTOR OUTPUT
        # ==========================================
        elif tool == "vector":
            summary = [
                r.get("content") for r in results
                if isinstance(r, dict)
            ]

            return {
                "answer": "Top relevant information found",
                "summary": summary
            }

    # ==========================================
    # 🔹 FALLBACK
    # ==========================================
    return {"answer": "No results found"}