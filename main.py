from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"} 

@app.get("/posts")
def get_post():
    return {"data": "Hello there!"}
