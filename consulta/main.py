from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
app = FastAPI()

fake_db = [{"item_name":"Foo"},{"item_name": "bar"},{"item_name":"baz"},{"item_name":"baz"}]

#http://127.0.0.1:8000/items/?skip=0&limit=1
@app.get("/items/")
async def items(skip: int = None, limit: int =None):
    if skip == None or limit == None:
        items = None
    else:
        items = fake_db[skip: skip+limit]
    cache_control = "no-cache, no-store, must-revalidate"
    #to tentando fazer com que o navegador atualize só aqui mas tá dificil
    return JSONResponse(content=items,headers={"Cache-Control": cache_control})

#parametros opcionais
#http://127.0.0.1:8000/new_items/obrigatorio?q=14
@app.get("/new_items/{item_id}")
async def new_items(item_id:str, q: str | None = None):
    if q:
        return {"item_id":item_id,"q":q}
    return {"item_id": item_id}

#Função Optional[tipo_da variavel]
@app.get("/items/{item_id}")
async def new_items_active(item_id: str, q : Optional[str] = None, short :bool = False):
    item = {"item_id":item_id}
    if q :
        item.update({"q":q})
    if short:
        item.update({"active": True})
    else:
        item.update({"active": False})
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int,q:Optional[str] = None,permition:bool = False):
    item = {}
    if user_id:
        if permition !=True:
            return {"fail":"você não tem permissão"}
        else:

            if item_id:
                item.update({"user":user_id, "item":item_id})
                if q:
                    item.update({"q":q})
                else:
                    pass
            else:
                return{"user":user_id, "not have item":"sorry"}
            item.update({"permition":True})
        return item

    else:
        return {"não há usuário"}

#multiplos parametros de consulta /\ como se o de cima tbm não tivesse isso...

#http://127.0.0.1:8000/items2/abc/?&needy=123&limit=1&skip=123 a posição das variaveis após ? 
#não muda a posição dos valores pois a eles é reservados o nome e não a posição que é entrege
@app.get("/items2/{item_id}/")
async def read_item(item_id: str, needy: str, skip : int = 0, limit:Optional[int] = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item