import os
from loaders.data_loader import load_all_data
from vector_store.build_index import build_faiss_index


def main():
    print("Starting FAISS index creation...")

    base_path = "dataset/bpss_agentic_dataset"

    if not os.path.exists(base_path):
        raise ValueError(f"Dataset path not found: {base_path}")

    print("Loading documents...")
    documents = load_all_data(base_path)

    if not documents:
        raise ValueError("No documents found. Check dataset folder.")

    print(f"Total documents loaded: {len(documents)}")

    print("Building FAISS index...")
    build_faiss_index(documents, save_path="faiss_index")

    print("Index successfully created!")


if __name__ == "__main__":
    main()