from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, get_db
import time
from .routers import post, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}