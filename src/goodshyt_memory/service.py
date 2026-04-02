from collections import Counter
from .models import MemoryCreate, MemoryLink, MemoryRecord, SummaryResponse
from .store import MemoryStore

class MemoryService:
    def __init__(self, store: MemoryStore | None = None) -> None:
        self.store = store or MemoryStore()

    def create_memory(self, payload: MemoryCreate) -> MemoryRecord:
        record = MemoryRecord(**payload.model_dump())
        return self.store.add_memory(record)

    def list_memories(self, user_id: str) -> list[MemoryRecord]:
        return self.store.list_memories(user_id)

    def link_memories(self, payload: MemoryLink) -> MemoryLink:
        return self.store.add_link(payload)

    def summarize(self, user_id: str) -> SummaryResponse:
        memories = self.list_memories(user_id)
        counter = Counter(m.kind for m in memories)
        return SummaryResponse(
            user_id=user_id,
            memory_count=len(memories),
            kinds=dict(counter),
            highlights=[m.content for m in memories[:5]],
        )
