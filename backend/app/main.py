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

@app.get("/notes")
def get_recent_notes(limit: int = Query(gt=0,lt=15,default=10)):
    return {
        "message" : "Recent notes retrieved successfully",
        "notes": notes_db[:limit]   

        }

@app.get("/notes/{note_id}")
def get_notes(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            return {
                "note" : note
            }
    return {
        "message" : "Note not found"
    }

@app.delete("notes/{note_id}")
def delete_note(note_id: int):
    for index,note in enumerate(notes_db):
        if note.id == note_id:
            del notes_db[index]
            return {
                "message" : "Note deleted successfully"
            }
    return {
        "message" : "Note not found"    
    }