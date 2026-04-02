from fastapi import FastAPI
from .models import MemoryCreate, MemoryLink
from .service import MemoryService

app = FastAPI(title="GoodShyt Memory", version="0.1.0")
service = MemoryService()

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "goodshyt-memory"}

@app.post("/memories")
def create_memory(payload: MemoryCreate) -> dict[str, object]:
    return {"memory": service.create_memory(payload).model_dump()}

@app.get("/memories/{user_id}")
def list_memories(user_id: str) -> dict[str, object]:
    memories = [m.model_dump() for m in service.list_memories(user_id)]
    return {"memories": memories, "count": len(memories)}

@app.get("/memories/{user_id}/summary")
def summarize(user_id: str) -> dict[str, object]:
    return service.summarize(user_id).model_dump()

@app.post("/links")
def link_memories(payload: MemoryLink) -> dict[str, object]:
    return {"link": service.link_memories(payload).model_dump()}
