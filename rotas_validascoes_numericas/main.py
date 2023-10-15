from fastapi import FastAPI,Path,Query
from typing import Union

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(
        title="Id do item dar get"),
    q: str | None = Query(
        default=None,
        alias="query-item")
):
    results= {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results
#http://127.0.0.1:8000/items/123?query-item=yes


#metadados
@app.get("/items1/{item_id}")
async def read_metadados(
    item_id: int  = Path(title="Id dar Get"),
    q: str = Query(default=None,alias="query-item"),
):
    results= {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

@app.get("/items2/{item_id}")
async def read_ordenado_items(
    q: str,
    item_id: int = Path(title="Item get")):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

# @app.get("/items3/{item_id}")
# async def read_acordo_necessidade(
#     q:str,
#     item_id: int = Path(title='GET ID',)
# )

#ordenaçao de parametros por truques
@app.get("/items4/{item_id}/")
async def read_at_tricks(
    *,
    item_id: int  = Path(title="my title of di"),
    q: str):

    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

#validation numerics
#gt = great then ge = great then or equal
#le = less then or equal lt less then
@app.get("/items5/{item_id}/")
async def numerical_with(*,item_id: int = Path(title = "id informaton",ge = 1),
                         q:str):
    results = {"item_id": item_id}
    if q:
        results.update({'q':q})
    return results

@app.get("/items6/{item_id}/")
async def numerical_0_a_1000(*,
                             item_id: int = Path(title="numerical get",gt=0,le=1000),
                             q:Union[str,None] = Query(default=None, alias='i')):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

#size estourou http://localhost:8000/items7/1/?q=123&size=10.9
#item estorou http://localhost:8000/items7/16/?q=123&size=10.4
#funcional http://localhost:8000/items7/14/?q=123&size=10.4
@app.get("/items7/{item_id}/")
async def read_items(
    *,
    item_id: int = Path(title="O ID para Get",gt=0,le=15),
    q:Union[str,None],
    size: float = Query(ge=0,lt=10.5),
):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
        return results