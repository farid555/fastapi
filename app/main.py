from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


# title str, content str

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


@app.get("/posts")
def get_post():
    return {"data": "Hello there!"}


@app.post("/createpost")
# collected the body and convert to dict then save in to payload
def create_post(post: Post):
    print(type(post))
    print(type(post.dict()))
    return {"data": f"new post {post}"}
