from vector_store.build_index import load_faiss_index

# ==========================================
# 🔹 LOAD FAISS INDEX (ONCE)
# ==========================================
INDEX_PATH = "faiss_index"
db = load_faiss_index(INDEX_PATH)


# ==========================================
# 🔹 VECTOR SEARCH TOOL
# ==========================================
def search_vector(query, k=3):
    """
    Perform semantic search on FAISS index
    """

    results = db.similarity_search(query, k=k)

    formatted_results = []

    for r in results:
        formatted_results.append({
            "content": r.page_content[:300],
            "source": r.metadata.get("source"),
            "type": r.metadata.get("type"),
            "path": r.metadata.get("path")
        })

    return formatted_results
