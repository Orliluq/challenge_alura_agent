from langchain_google_genai import ChatGoogleGenerativeAI
# from transformers import pipeline
# from langchain_huggingface import HuggingFacePipeline

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

VECTORSTORE_DIR = "vectorstore"

# -------------------------
# Embeddings
# -------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

db = FAISS.load_local(
    VECTORSTORE_DIR,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={
        "k": 2
    }
)

# -------------------------
# LLM GOOGLE GEMINI
# -------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# -------------------------
# LLM LOCAL
# -------------------------
# pipe = pipeline(
#     "text-generation",
#     model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     max_new_tokens=32,
#     do_sample=False,
#     temperature=0
# ) 

# llm = HuggingFacePipeline(pipeline=pipe)

# -------------------------
# PROMPT
# -------------------------
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Eres un asistente corporativo de una empresa.

Usa SOLO el contexto para responder.

Si no sabes la respuesta, di: "No tengo información suficiente".

Contexto:
{context}

Pregunta:
{question}

Respuesta clara:
"""
)

# -------------------------
# QA CHAIN
# -------------------------
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)


def ask_question(question: str):
    try:
        print("1. Iniciando búsqueda")

        result = qa_chain.invoke(
            {"query": question}
        )

        print("2. Terminó invoke")

        answer = result["result"]

        sources = list(
            {
                doc.metadata.get(
                    "source",
                    "desconocido"
                )
                for doc in result["source_documents"]
            }
        )

        return {
            "question": question,
            "answer": answer,
            "sources": sources
        }

    except Exception as e:

        print(e)

        return {
            "answer": f"Error: {str(e)}",  
            "sources": [],                   
            "question": question,
        }