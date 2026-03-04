from fastapi import FastAPI

app = FastAPI(title="DevOps Portfolio API", version="1.0.0")

FAKE_DB = [{"id": 1, "name": "hello-devops"}]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return {"items": FAKE_DB}

@app.post("/items")
def create_item(name: str):
    new_id = max(i["id"] for i in FAKE_DB) + 1 if FAKE_DB else 1
    item = {"id": new_id, "name": name}
    FAKE_DB.append(item)
    return item