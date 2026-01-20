from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address 
import models
from database import engine
from routers import user, todo

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

limiter = Limiter(key_func = get_remote_address)
app.state.limiter = limiter

app.include_router(user.router)
app.include_router(todo.router)
