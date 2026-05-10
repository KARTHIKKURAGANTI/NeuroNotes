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

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    msg: str