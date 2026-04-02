from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4
from pydantic import BaseModel, Field

MemoryKind = Literal["preference", "fact", "goal", "constraint", "relationship", "note"]
TrustLevel = Literal["low", "medium", "high"]

class MemoryCreate(BaseModel):
    user_id: str = Field(min_length=1)
    content: str = Field(min_length=1)
    kind: MemoryKind
    tags: list[str] = []
    trust: TrustLevel = "medium"

class MemoryRecord(MemoryCreate):
    memory_id: str = Field(default_factory=lambda: uuid4().hex)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class MemoryLink(BaseModel):
    source_memory_id: str
    target_memory_id: str
    relation: str

class SummaryResponse(BaseModel):
    user_id: str
    memory_count: int
    kinds: dict[str, int]
    highlights: list[str]
