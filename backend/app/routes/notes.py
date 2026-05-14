from fastapi import APIRouter, HTTPException, status,Query,Depends
from typing import List
from app import schemas,models
from app.database import get_db
from sqlalchemy.orm import Session  

router = APIRouter()



@router.post("/notes",status_code=201)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    new_note=models.Note(
        title = note.title,
        content = note.content
    )
    
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return {"mesaage":"Note created successfully"}

"""@router.get("/notes",response_model=List[NoteResponse])
def get_recent_notes(limit: int = Query(gt=0,lt=15,default=10)):
    return notes_db[:limit]

@router.get("/notes/{note_id}",response_model=NoteResponse)
def get_notes(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404,detail="Note not found")  

@router.delete("/notes/{note_id}",status_code=204)
def delete_note(note_id: int):
    for index,note in enumerate(notes_db):
        if note["id"] == note_id:
            del notes_db[index]
            return 
    raise HTTPException(status_code=404,detail="Note not found")"""