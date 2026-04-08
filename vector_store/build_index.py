from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


# ==========================================
# 🔹 GET EMBEDDING MODEL (FREE)
# ==========================================
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# ==========================================
# 🔹 BUILD FAISS INDEX
# ==========================================
def build_faiss_index(documents, save_path="faiss_index"):

    print("🔹 Splitting documents into chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    split_docs = splitter.split_documents(documents)

    print(f"✅ Total chunks created: {len(split_docs)}")

    print("🔹 Creating embeddings (HuggingFace - FREE)...")

    embeddings = get_embeddings()

    print("🔹 Building FAISS index...")

    db = FAISS.from_documents(split_docs, embeddings)

    # Save index locally
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    db.save_local(save_path)

    print(f"✅ FAISS index saved at: {save_path}")

    return db


# ==========================================
# 🔹 LOAD EXISTING INDEX
# ==========================================
def load_faiss_index(path="faiss_index"):

    print("🔹 Loading FAISS index...")

    embeddings = get_embeddings()

    db = FAISS.load_local(
        path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("✅ FAISS index loaded")

    return db