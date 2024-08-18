from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def home() -> str:
    return "Hello, world!"
