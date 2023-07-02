from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!!"}


@app.get("/posts")
def get_post():
    return {"data": "Hello there!"}


@app.post("/createpost")
# collected the body and convert to dict then save in to payload
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": f"Successfully create post {payload}"}
