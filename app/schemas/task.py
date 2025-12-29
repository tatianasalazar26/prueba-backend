from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
