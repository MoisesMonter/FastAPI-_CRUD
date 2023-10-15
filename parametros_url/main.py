from fastapi import FastAPI
from modelname import ModelName as models_name


app = FastAPI()

global_me =["nome","idade","genero"]
dict_user ={1:["marcos","60","tanke de guerra nao binarie que voa"]}

from enum import Enum

class genero(str,Enum):
    masculino = "m"
    
    feminino  = "f"


@app.get("/{item_id}")
async def read_iem(item_id: str):
    return {"curioso você digitar": item_id}

@app.get("/user/me")
async def user():
    return{"information":global_me}

@app.get("/user/{id}")
async def user_by_id(id:int):
    return{dict_user[1][0]:"informations"+str(dict_user[1][1:])}


#valores predefinidos  1
@app.get("/models/{model_name}")
async def models(model_name: models_name):
    if model_name is models_name.moises:
        return {model_name: "larga noite de estudo para noite de vigilante"}
    elif model_name is models_name.leonardo:
        return {model_name: "tem uma grande afinidade com programação, só não é de falar muito"}
    elif model_name is models_name.talismar:
        return{model_name: "dá bronca nos professores até de atestado em casa, com esse cara não se brinca!"}



#valores predefinidos  2
@app.get("/generos/{gen}")
async def get_model(gen: genero):
    if gen is genero.masculino:
        return {"você informou Masculino de":gen}
    return {"você informou Feminino de":gen}

#Conversor de rota
@app.get("/files/{file_path:path}")
async def files(file_path: str):
    return {"file_path": file_path}