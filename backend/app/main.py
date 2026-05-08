from fastapi import FastAPI,Path,Query
from .schemas import NoteCreate, NoteResponse
from typing import List
from fastapi import HTTPException,status
app = FastAPI()
 
from app.routes import notes
app.include_router(notes.router, prefix="/notes", tags=["Notes"])

# Health check endpoint
@app.get("/health")
def health():

    return {
        "status" : "ok"
    }

# Home endpoint
@app.get("/")
def home():
    return {
        "message" : "Welcome to Neuronotes API"
    }

