from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    result = {"items": [{"item_id":"Foo"},{"item_id":"bar"}]}
    if q: 
        result.update({"q":q})
    return result

@app.get("/items1/")
async def read_items_limit(q: Union[str,None] = Query(default=None,max_length=50)):
    result = {"items": [{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result

@app.get("/items2/")
async def read_items_two_limit(q: Union[str,None] = Query(default=None,min_length=3,max_length=10)):
    result = {"items": [{"item_id":"Foo"},{"item_id":"bar"}]}
    if q:
        result.update({"q":q})
    return result

#filtragem query regex
import re
@app.get("/items3/")
async def read_items_patterns(q: Union[str,None] = Query(default=None,min_length=3,max_length=7,regex="^[a-zA-Z][a-zA-Z0-9]*$")):
    result = {"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        if re.search(r'[A-Z]',q):
            result.update({"q":q})
            return result
        return "422 Unprocessable Entity"

# lista parametros de multiplos valores
@app.get("/items4/")
async def read_items_list(q: Union[list[str],None] = Query(DEFAULT=None)):
    Query_items = {"q":q}
    return Query_items

# lista parametros de multiplos valores já predefinidos

@app.get("/items5/")
async def read_predef_items(q: list[str] = Query(default=["foo","bar"])):
    Query_items = {"q":q}
    return Query_items

# assim pode vir vasio 
@app.get("/items6/")
async def read_list_items(q:list = Query(default=[])):
    Query_items = {"q": q}
    return Query_items

#titulo e descrição
@app.get("/items7/")
async def read_list_title(q : Union[str,None] = Query(default=None,
                                                      title="Query String",
                                                      description="Query string for the items to search in the database that have a good match", 
                                                      min_length=3)):
    Query_items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        Query_items.update({"q":q})
    return Query_items

#apelidos, além do mais os apelidos podem ser petitivos,
#  dessa maneira tem que seguir o padrão como as variaveis são consumidas, primeiro q depois o b
# ambos são chamaos item-Query
@app.get("/items8/")
async def read_apelido_title(
    q:Union[str,None] = Query(
        default=None,
        alias="item-Query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=10,
        regex="^[a-zA-Z][a-zA-Z0-9]*$",
        deprecated=True #Deprecated fornece a função dessa documentação ser descontinuado.
        ),
    b:Union[str,None] = Query(
        default=None,
        alias="item-Query",
        title="Query-string2",
        description="Query string for the items to search in the database that have a good match 2",
        deprecated=True,
    ) ):
    Query_items = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        Query_items.update({"q":q})
    if b:
        Query_items.update({"b":b})
    return Query_items