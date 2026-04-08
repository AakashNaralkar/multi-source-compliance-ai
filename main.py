# # from loaders.data_loader import load_all_data

# # docs = load_all_data("dataset/bpss_agentic_dataset")

# # print(len(docs))
# # print(docs[0])
# # for d in docs[:3]:
# #     print(d.metadata)


# from loaders.data_loader import load_all_data
# from vector_store.build_index import build_faiss_index, load_faiss_index
# import os


# # ==========================================
# # 🔹 CONFIG
# # ==========================================
# DATA_PATH = "dataset/bpss_agentic_dataset"
# INDEX_PATH = "faiss_index"


# # ==========================================
# # 🔹 MAIN PIPELINE
# # ==========================================
# def main():

#     # Step 1: Load data
#     docs = load_all_data(DATA_PATH)

#     print(f"\n📊 Documents loaded: {len(docs)}")

#     # Step 2: Build or Load FAISS index
#     if os.path.exists(INDEX_PATH):
#         print("\n⚡ Loading existing FAISS index...")
#         db = load_faiss_index(INDEX_PATH)
#     else:
#         print("\n🚀 Building new FAISS index...")
#         db = build_faiss_index(docs, INDEX_PATH)

#     # Step 3: Test retrieval (IMPORTANT)
#     while True:
#         query = input("\n🔍 Ask a question (or type 'exit'): ")

#         if query.lower() == "exit":
#             break

#         results = db.similarity_search(query, k=3)

#         print("\n📄 Top Results:\n")

#         for i, r in enumerate(results):
#             print(f"--- Result {i+1} ---")
#             print(f"Source: {r.metadata}")
#             print(f"Content: {r.page_content[:300]}...\n")


# # ==========================================
# # 🔹 RUN
# # ==========================================
# if __name__ == "__main__":
#     main()


from loaders.data_loader import load_all_data
from vector_store.build_index import build_faiss_index, load_faiss_index
from agent.agent import run_agent
import os
import json


# ==========================================
# 🔹 CONFIG
# ==========================================
DATA_PATH = "dataset/bpss_agentic_dataset"
INDEX_PATH = "faiss_index"


# ==========================================
# 🔹 MAIN PIPELINE
# ==========================================
def main():

    print("\n🚀 Starting AI Agent System...\n")

    # ==========================================
    # 🔹 STEP 1: LOAD DATA
    # ==========================================
    docs = load_all_data(DATA_PATH)
    print(f"\n📊 Documents loaded: {len(docs)}")

    # ==========================================
    # 🔹 STEP 2: BUILD / LOAD FAISS
    # ==========================================
    if os.path.exists(INDEX_PATH):
        print("\n⚡ Loading existing FAISS index...")
        db = load_faiss_index(INDEX_PATH)
    else:
        print("\n🚀 Building new FAISS index...")
        db = build_faiss_index(docs, INDEX_PATH)

    print("\n✅ System Ready!")

    # ==========================================
    # 🔹 STEP 3: AGENT LOOP
    # ==========================================
    while True:
        query = input("\n🔍 Ask a question (or type 'exit'): ")

        if query.lower() == "exit":
            print("\n👋 Exiting system...")
            break

        try:
            # 🔥 AGENT CALL
            result = run_agent(query)

            print("\n📢 FINAL ANSWER:\n")

            # ==========================================
            # 🔥 CLEAN OUTPUT (VERY IMPORTANT)
            # ==========================================
            print(json.dumps(result, indent=2))

        except Exception as e:
            print("\n❌ Error during processing:")
            print(str(e))


# ==========================================
# 🔹 RUN
# ==========================================
if __name__ == "__main__":
    main()