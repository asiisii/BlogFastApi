from fastapi import FastAPI

app = FastAPI()  # main point of interaction to create all APIs


@app.get("/")
async def root():
    return {"msg": "Hello, world!"}
