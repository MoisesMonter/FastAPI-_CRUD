from fastapi import FastAPI
from modelname import ModelName as models_name
app = FastAPI()

@app.get("/")
async def my_first_root():
    return {"messsagem":"primeiro Hello do FastAPI"}

@app.get("/{item_id}")
async def read_iem(item_id: str):
    return {"curioso você digitar": item_id}

#Condicionar rotas

@app.get("/users/me")
async def read_user_me():
    return {"user_id":"Você não entrou como id"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"hello ": user_id[0:3]}


#valores predefinidos
@app.get("/models/{model_name}")
async def get_model(model_name: models_name):
    if model_name is models_name.moises:
        return {model_name: "larga noite de estudo para noite de vigilante"}
    elif model_name is models_name.leonardo:
        return {model_name: "tem uma grande afinidade com programação, só não é de falar muito"}
    elif model_name is models_name.talismar:
        return{model_name: "dá bronca nos professores até de atestado em casa, com esse cara não se brinca!"}

#Conversor de rota
@app.get("files//home/path/{file_path:path}")
async def read_file_home(file_path:str):
    return {"file_path": file_path}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}