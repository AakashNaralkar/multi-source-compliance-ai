from tools.vector_tool import search_vector

def search_policy(query):
    """
    Search only policy-related content
    """

    print("Searching policies...")

    results = search_vector(query, k=5)

    # Filter only policy docs
    policy_results = [
        r for r in results
        if r.get("type") == "pdf" or r.get("type") == "docx"
    ]

    if not policy_results:
        return ["No relevant policy found"]

    return policy_results

def interpret_policy(query):
    """
    Convert policy text into actionable answer
    """

    results = search_policy(query)

    if isinstance(results, list) and isinstance(results[0], str):
        return results

    final_answer = []

    for r in results:
        content = r.get("content", "").lower()

        if "must" in content or "mandatory" in content:
            decision = "Required"

        elif "optional" in content or "may" in content:
            decision = "Optional"

        elif "not required" in content or "not mandatory" in content:
            decision = "Not Required"

        else:
            decision = "Check manually"

        final_answer.append({
            "decision": decision,
            "source": r.get("source"),
            "snippet": r.get("content")
        })

    return final_answer

def check_policy(query):
    """
    Main entry point for agent
    """

    print("Running policy check...")

    interpreted = interpret_policy(query)

    return interpreted