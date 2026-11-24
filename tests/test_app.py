from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_ask_pending_pod():
    r = client.post("/ask", json={"question": "my pod is pending"})
    assert r.status_code == 200
    assert r.json()["source"] == "pending-pod.md"


def test_ask_no_match():
    r = client.post("/ask", json={"question": "banana"})
    assert r.json()["source"] is None