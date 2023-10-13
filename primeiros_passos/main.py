import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def my_first_root():
    return {"messsagem":"primeiro Hello do FastAPI"}
    
