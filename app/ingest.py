from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_DIR = Path("data")
VECTORSTORE_DIR = "vectorstore"

# =========================
# LOAD PDFS
# =========================
def load_documents():
    docs = []

    for pdf_file in DATA_DIR.glob("*.pdf"):
        reader = PdfReader(pdf_file)

        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        docs.append(
            Document(
                page_content=text,
                metadata={"source": pdf_file.name}
            )
        )

    return docs


# =========================
# MAIN INGEST PIPELINE
# =========================
def main():
    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    db = FAISS.from_documents(
        chunks,
        embedding=embeddings
    )

    db.save_local(VECTORSTORE_DIR)

    print("✅ Vectorstore creado correctamente")


if __name__ == "__main__":
    main()
from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_DIR = Path("data")
VECTORSTORE_DIR = "vectorstore"

# =========================
# LOAD PDFS
# =========================
def load_documents():
    docs = []

    for pdf_file in DATA_DIR.glob("*.pdf"):
        reader = PdfReader(pdf_file)

        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        docs.append(
            Document(
                page_content=text,
                metadata={"source": pdf_file.name}
            )
        )

    return docs


# =========================
# MAIN INGEST PIPELINE
# =========================
def main():
    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    db = FAISS.from_documents(
        chunks,
        embedding=embeddings
    )

    db.save_local(VECTORSTORE_DIR)

    print("✅ Vectorstore creado correctamente")


if __name__ == "__main__":
    main()