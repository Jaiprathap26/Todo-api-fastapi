from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"


pwd_context = CryptContext(
    schemes = ["bcrypt"], deprecated = "auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])

def verify_password(password, hashed) -> bool:
    return pwd_context.verify(password[:72], hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

