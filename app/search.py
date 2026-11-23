import math
import re
from collections import Counter
from pathlib import Path

RUNBOOK_DIR = Path(__file__).resolve().parent.parent / "runbooks"

STOP = {
    "the", "a", "an", "is", "are", "to", "of", "and", "or", "in", "on", "it",
    "my", "not", "for", "with", "how", "do", "i", "does", "what", "why",
    "can", "you", "at", "be", "by", "if", "then", "this", "that", "from",
}


def tokenize(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [w for w in words if w not in STOP and len(w) > 1]


def load_docs():
    docs = []
    for path in sorted(RUNBOOK_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        docs.append({"name": path.name, "text": text, "tokens": tokenize(text)})
    return docs


def search(query, top_k=1):
    docs = load_docs()
    n = len(docs)
    df = Counter()
    for d in docs:
        df.update(set(d["tokens"]))
    q_tokens = tokenize(query)
    results = []
    for d in docs:
        tf = Counter(d["tokens"])
        score = 0.0
        for t in q_tokens:
            if t in tf:
                idf = math.log((n + 1) / (df[t] + 1)) + 1
                score += (tf[t] / len(d["tokens"])) * idf
        results.append({"name": d["name"], "score": round(score, 4), "text": d["text"]})
    results.sort(key=lambda r: r["score"], reverse=True)
    return [r for r in results[:top_k] if r["score"] > 0]