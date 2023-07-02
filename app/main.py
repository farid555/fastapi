from random import randrange
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


my_posts = [{"title": "title for post 1", "content": "this from content 1", "id": 1},
            {"title": "title for post 2", "content": "this from content 2", "id": 2}]  # Array of dict


def find_Post(id):
    for p in my_posts:
        if p['id'] == id:
            print(p)
            return p


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/post/{id}")
def get_post(id: int):
    post = find_Post(int(id))
    print(post)
    return {"data": f"this the post {post}"}


@app.post("/post") # collected the body and convert to dict then save in to payload
def create_post(post: Post):
    print(post)
    post_dict = (post.dict())
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": f"new post {post_dict}"}