from fastapi import FastAPI

app = FastAPI()

#primeiros passos

@app.get("/")
async def my_first_root():
    return {"messsagem":"primeiro Hello do FastAPI"}