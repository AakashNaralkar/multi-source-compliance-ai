from langchain_core.documents import Document
import pandas as pd
from pypdf import PdfReader
import os

def load_pdfs(folder_path):
    documents = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, file))
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            documents.append(
                Document(
                    page_content=text,
                    metadata={"source": file, "type": "pdf"}
                )
            )
    return documents