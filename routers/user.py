from slowapi import Limiter 
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import SECRET_KEY, ALGORITHM
from jose import jwt
from schemas import UserCreate, UserLogin
from models import User
from database import SessionLocal
from auth import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    
    db = SessionLocal()
    
    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise HTTPException(status_code = 400, detail = "Email already exists")
    
    new_user = User(
        name = user.name,
        email =  user.email,
        password = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token({"id": new_user.id})
    return {"token": token}

@router.post("/refresh")
def refresh_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    new_access_token = create_access_token({"id": payload["id"]})
    return {"token": new_access_token}

@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):
        db.close()
        raise HTTPException(status_code= 401, detail= "Invalid credentials")
    
    token = create_access_token({"id": db_user.id})

    db.close()
    return {"token": token}