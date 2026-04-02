import json
from pathlib import Path
from .models import MemoryLink, MemoryRecord

class MemoryStore:
    def __init__(self, filepath: str = "data/memory_store.json") -> None:
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        if not self.filepath.exists():
            self.filepath.write_text(json.dumps({"memories": [], "links": []}, indent=2), encoding="utf-8")

    def _load(self) -> dict[str, list[dict]]:
        return json.loads(self.filepath.read_text(encoding="utf-8"))

    def _save(self, payload: dict[str, list[dict]]) -> None:
        self.filepath.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def add_memory(self, record: MemoryRecord) -> MemoryRecord:
        data = self._load()
        data["memories"].append(record.model_dump())
        self._save(data)
        return record

    def list_memories(self, user_id: str) -> list[MemoryRecord]:
        data = self._load()
        return [MemoryRecord.model_validate(item) for item in data["memories"] if item["user_id"] == user_id]

    def add_link(self, link: MemoryLink) -> MemoryLink:
        data = self._load()
        data["links"].append(link.model_dump())
        self._save(data)
        return link
