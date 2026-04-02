from goodshyt_memory.models import MemoryCreate
from goodshyt_memory.service import MemoryService
from goodshyt_memory.store import MemoryStore

def test_create_and_summarize(tmp_path) -> None:
    service = MemoryService(store=MemoryStore(filepath=str(tmp_path / "memory.json")))
    service.create_memory(MemoryCreate(user_id="demo", content="User prefers concise updates", kind="preference"))
    summary = service.summarize("demo")
    assert summary.memory_count == 1
    assert summary.kinds["preference"] == 1
