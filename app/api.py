from fastapi import FastAPI
from app.models import QuestionRequest, QuestionResponse
from app.rag import ask_question

app = FastAPI(
    title="Santos Pegasus AI Agent",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Santos Pegasus AI Agent funcionando. Chiquis está vivoooo!!",
        "status": "ok"
    }

@app.post("/ask", response_model=QuestionResponse)
def ask(payload: QuestionRequest):
    response = ask_question(payload.question)
    return QuestionResponse(**response)