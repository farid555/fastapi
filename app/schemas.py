from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostRespons(PostBase):
    # id: int
    title: str
    content: str
    published: bool = True
    # created_at: datetime

    class Config:    # make sure it's right indent
        orm_mode = True
