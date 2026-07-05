from pathlib import Path

from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# ============================================
# CONFIGURACIÓN
# ============================================

DATA_DIR = Path("data")
VECTORSTORE_DIR = Path("vectorstore")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# ============================================
# CARGA DE DOCUMENTOS
# ============================================

def load_documents() -> list[Document]:
    """
    Lee todos los PDF de la carpeta data y los convierte en documentos.
    """

    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"No existe la carpeta '{DATA_DIR.resolve()}'"
        )

    pdf_files = list(DATA_DIR.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "No se encontraron archivos PDF dentro de la carpeta data/"
        )

    documents = []

    for pdf_file in pdf_files:

        print(f"📄 Leyendo: {pdf_file.name}")

        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": pdf_file.name
                }
            )
        )

    print(f"\n✅ PDFs cargados: {len(documents)}")

    return documents


# ============================================
# CREAR CHUNKS
# ============================================

def split_documents(documents: list[Document]) -> list[Document]:
    """
    Divide los documentos en fragmentos para mejorar el RAG.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Chunks creados: {len(chunks)}")

    return chunks


# ============================================
# CREAR VECTORSTORE
# ============================================

def create_vectorstore(chunks: list[Document]) -> None:
    """
    Genera el índice FAISS.
    """

    print("🧠 Cargando modelo de embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )

    print("📦 Generando embeddings...")

    db = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    VECTORSTORE_DIR.mkdir(exist_ok=True)

    db.save_local(str(VECTORSTORE_DIR))

    print(f"✅ Vectorstore guardado en: {VECTORSTORE_DIR.resolve()}")


# ============================================
# MAIN
# ============================================

def main():

    print("=" * 60)
    print("🚀 Iniciando proceso de indexación")
    print("=" * 60)

    documents = load_documents()

    chunks = split_documents(documents)

    create_vectorstore(chunks)

    print("=" * 60)
    print("🎉 Proceso completado correctamente")
    print("=" * 60)


if __name__ == "__main__":
    main()