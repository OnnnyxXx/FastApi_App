from typing import Optional

from pydantic import BaseModel


class STasksAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STasksAdd):
    id: int


class STaskID(BaseModel):
    ok: bool = True
    tasks_id: int
