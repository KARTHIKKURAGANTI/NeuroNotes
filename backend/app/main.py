from fastapi import FastAPI,Path,Query
from .schemas import NoteCreate, NoteResponse
from typing import List
from fastapi import HTTPException,status
app = FastAPI()
notes_db = []  # In-memory database for notes

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

@app.post("/notes",response_model=NoteResponse,status_code=201)
def create_note(note: NoteCreate):
    new_note={
        "id" : len(notes_db)+1,
        "title" : note.title,
        "content" : note.content,
        "tag": note.summary
    }
    notes_db.append(new_note)
    return new_note

@app.get("/notes",response_model=List[NoteResponse])
def get_recent_notes(limit: int = Query(gt=0,lt=15,default=10)):
    return notes_db[:limit]

@app.get("/notes/{note_id}",response_model=NoteResponse)
def get_notes(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404,detail="Note not found")  

@app.delete("/notes/{note_id}",status_code=204)
def delete_note(note_id: int):
    for index,note in enumerate(notes_db):
        if note["id"] == note_id:
            del notes_db[index]
            return 
    raise HTTPException(status_code=404,detail="Note not found")