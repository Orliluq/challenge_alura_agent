from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import QuestionRequest, QuestionResponse

app = FastAPI(
    title="Santos Pegasus AI Agent",
    version="1.0.0"
)

# Configurar CORS  
app.add_middleware(
    CORSMiddleware,       
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

print('CORS agregado correctamente')

@app.get("/")
def root():
    return {
        "message": "Santos Pegasus AI Agent funcionando. Chiquis está vivoooo!!",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=QuestionResponse)
def ask(payload: QuestionRequest):
    from app.rag import ask_question

    response = ask_question(payload.question)
    return QuestionResponse(**response)