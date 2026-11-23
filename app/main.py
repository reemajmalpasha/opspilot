from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="OpsPilot")

class Question(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: Question):
    return {"answer": f"(mock) You asked: {q.question}"}
