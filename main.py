import os
from agent.llm_agent import run_llm_agent


if __name__ == "__main__":
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Check your .env file!")

    while True:
        q = input("\n Ask: ")

        if q.lower() == "exit":
            break

        answer = run_llm_agent(q)

        print("\n RESULT:\n")
        print(answer)