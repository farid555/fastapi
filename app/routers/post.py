from ..database import  get_db
from typing import  List
from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import  Response, status, HTTPException, Depends, APIRouter


router = APIRouter()



@router.get("/posts", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    print(posts)

    return posts


@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = models.Post(**post.dict())
    db.add(new_post)  # add to the database
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/posts/{id}", response_model=schemas.PostResponse)
def get_post(id: int, response: Response, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return post


@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,  db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post.delete(synchronize_session=False)

    db.commit()


@router.put("/posts/{id}",  response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post_find = post_query.first()

    if post_find == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_query.update(post.dict(), synchronize_session=False)

    db.commit()

    return post_query.first()
