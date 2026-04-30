from fastapi import FastAPI,Path,Query
from schemas import NoteCreate, NoteResponse

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

@app.post("/notes")
def create_note(note: NoteCreate):
    new_note={
        "id" : len(notes_db),
        "title" : note.title,
        "content" : note.content
    }
    notes_db.append(note)
    return {
        "message" : "Note created successfully",
        "note" : note
    }

@app.get("/notes/{note_id}")
def get_notes(note_id: int):
    if note_id < 0 or note_id >= len(notes_db):
        return {
            "error" : "Note not found"
        }
    return {
        "notes" : notes_db[note_id]
    }