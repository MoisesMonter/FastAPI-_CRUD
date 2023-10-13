from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"messsagem":"primeiro Hello do FastAPI"}