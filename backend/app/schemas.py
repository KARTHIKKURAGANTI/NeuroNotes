from pydantic import BaseModel
from typing import Optional 

class NoteCreate(BaseModel):
    title: str
    content: str
    summary:Optional[str]=None

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str