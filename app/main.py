from fastapi import FastAPI
from pydantic import BaseModel

from app.search import search

app = FastAPI(title="OpsPilot")


class Question(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(q: Question):
    matches = search(q.question, top_k=1)
    if not matches:
        return {"answer": "No matching runbook found.", "source": None}
    best = matches[0]
    return {"answer": best["text"], "source": best["name"], "score": best["score"]}