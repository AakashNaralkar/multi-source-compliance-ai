# from loaders.data_loader import load_all_data

# docs = load_all_data("dataset/bpss_agentic_dataset")

# print(len(docs))
# print(docs[0])
# for d in docs[:3]:
#     print(d.metadata)


from loaders.data_loader import load_all_data
from vector_store.build_index import build_faiss_index, load_faiss_index
import os


# ==========================================
# 🔹 CONFIG
# ==========================================
DATA_PATH = "dataset/bpss_agentic_dataset"
INDEX_PATH = "faiss_index"


# ==========================================
# 🔹 MAIN PIPELINE
# ==========================================
def main():

    # Step 1: Load data
    docs = load_all_data(DATA_PATH)

    print(f"\n📊 Documents loaded: {len(docs)}")

    # Step 2: Build or Load FAISS index
    if os.path.exists(INDEX_PATH):
        print("\n⚡ Loading existing FAISS index...")
        db = load_faiss_index(INDEX_PATH)
    else:
        print("\n🚀 Building new FAISS index...")
        db = build_faiss_index(docs, INDEX_PATH)

    # Step 3: Test retrieval (IMPORTANT)
    while True:
        query = input("\n🔍 Ask a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        results = db.similarity_search(query, k=3)

        print("\n📄 Top Results:\n")

        for i, r in enumerate(results):
            print(f"--- Result {i+1} ---")
            print(f"Source: {r.metadata}")
            print(f"Content: {r.page_content[:300]}...\n")


# ==========================================
# 🔹 RUN
# ==========================================
if __name__ == "__main__":
    main()