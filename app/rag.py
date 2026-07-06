from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

VECTORSTORE_DIR = "vectorstore"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ============================================================
# CACHE GLOBAL
# ============================================================

qa_chain = None


# ============================================================
# CREAR QA CHAIN SOLO UNA VEZ
# ============================================================

def get_qa_chain():
    global qa_chain

    if qa_chain is None:

        from langchain_google_genai import ChatGoogleGenerativeAI
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_community.vectorstores import FAISS
        from langchain.chains import RetrievalQA
        from langchain_core.prompts import PromptTemplate

        print("=" * 60)
        print("🚀 Inicializando RAG...")
        print("=" * 60)

        # Validar que el vectorstore existe
        vectorstore_path = Path(VECTORSTORE_DIR)
        if not vectorstore_path.exists():
            raise FileNotFoundError(
                f"El directorio de vectorstore '{VECTORSTORE_DIR}' no existe. "
                "Ejecuta primero el script de ingestión para crear los índices."
            )

        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
Eres un asistente corporativo de Santos Pegasus Soluciones.

Prioriza responder utilizando la información proporcionada en el contexto.
Si el contexto contiene información relevante, úsala para responder.

Si el contexto NO contiene suficiente información para responder,
puedes usar tu conocimiento general sobre Santos Pegasus Soluciones,
pero siempre menciona que la respuesta no está basada en la documentación.

Contexto:
{context}

Pregunta:
{question}

Respuesta:
"""
        )

        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

        print("✅ Embeddings cargados")

        db = FAISS.load_local(
            VECTORSTORE_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )

        print("✅ Vectorstore cargado")

        retriever = db.as_retriever(
            search_kwargs={
                "k": 4
            }
        )

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

        print("✅ Gemini inicializado")

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            chain_type="stuff",
            return_source_documents=True,
            chain_type_kwargs={
                "prompt": prompt
            }
        )

        print("✅ QA Chain lista")
        print("=" * 60)

    return qa_chain


# ============================================================
# CONSULTA
# ============================================================

def ask_question(question: str):

    try:

        print(f"\n📨 Pregunta recibida:")
        print(question)

        chain = get_qa_chain()

        result = chain.invoke(
            {
                "query": question
            }
        )

        answer = result.get(
            "result",
            "No se obtuvo respuesta."
        )

        sources = sorted(
            {
                doc.metadata.get(
                    "source",
                    "desconocido"
                )
                for doc in result.get(
                    "source_documents",
                    []
                )
            }
        )

        return {
            "success": True,
            "question": question,
            "answer": answer,
            "sources": sources
        }

    except Exception as e:

        print("❌ ERROR")
        print(e)

        return {
            "success": False,
            "question": question,
            "answer": str(e),
            "sources": []
        }