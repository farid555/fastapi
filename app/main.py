from random import randrange
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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
            {"title": "title for post 2", "content": "this from content 2", "id": 2},
            {"title": "title for post 3", "content": "this from content 2", "id": 3},
            {"title": "title for post 4", "content": "this from content 2", "id": 4}]  # Array of dict


def find_Post(id):
    for p in my_posts:
        print(f"p-{p}")
        if p['id'] == id:
            print(id)
            return p


def find_post_index_id(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = (post.dict())
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": f"new post {post_dict}"}


@app.get("/post/{id}")
def get_post(id: int, response: Response):
    post = find_Post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_detail": post}


@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_post_index_id(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/post/{id}")
def update_post(id: int, post: Post):
    index = find_post_index_id(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_dict = post.dict()  # Convert to dict
    post_dict['id'] = id  # Add the id
    my_posts[index] = post_dict  # update
    return {"data": post_dict}
