from  import BaseModel


'''
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
   #rating: Optional[int] = None
   
class CreatePost(BaseModel):
    title: str
    content: str
    published: bool = True
    
class UpdatePost(BaseModel):
    published: bool = True
    
'''

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
class PostCreate(PostBase):
    pass

