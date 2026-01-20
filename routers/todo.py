from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Todo
from schemas import TodoCreate, TodoUpdate
from dependencies import get_current_user

router = APIRouter()


@router.post("/todos")
def create_todo(todo: TodoCreate, user=Depends(get_current_user)):
    db = SessionLocal()


    new_todo = Todo(
        title = todo.title,
        description = todo.description,
        owner_id = user["id"]
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    db.close()
    
    return new_todo

@router.get("/todos")
def get_todos(
    page: int = 1,
    limit: int = 10,
    search: str | None = None,
    sort: str = "desc",
    user=Depends(get_current_user)
):
    db = SessionLocal()

    offset = (page - 1) * limit

    # ✅ ALWAYS initialize query FIRST
    query = db.query(Todo).filter(Todo.owner_id == user["id"])

    # ✅ Apply search filter
    if search:
        query = query.filter(Todo.title.contains(search))

    # ✅ Apply sorting
    if sort == "asc":
        query = query.order_by(Todo.id.asc())
    else:
        query = query.order_by(Todo.id.desc())

    todos = query.offset(offset).limit(limit).all()
    total = query.count()

    db.close()

    return {
        "data": todos,
        "page": page,
        "limit": limit,
        "total": total
    }

@router.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    user = Depends(get_current_user)
):
    db = SessionLocal()

    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not db_todo:
        db.close()
        raise HTTPException(status_code = 404, detail = "Forbidden")
    
    db_todo.title = todo.title 
    db_todo.description = todo.description

    db.commit()
    db.refresh(db_todo)
    db.close()

    return db_todo 

@router.delete("/todos/{todo_id}",status_code = 204)
def delete_todo(
    todo_id: int,
    user = Depends(get_current_user)
):
    db = SessionLocal()

    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not db_todo:
        db.close()
        raise HTTPException(statuse_code = 404, detail = "Todo not found")
    
    if db_todo.owner_id != user["id"]:
        db.close()
        raise HTTPException(statuse_code = 403, detail = "Frobidden")
    
    db.delete(db_todo)
    db.commit()
    db.close()