from fastapi import FastAPI
from modelitem import Item as items

app = FastAPI()

#primeiros passos

@app.get("/")
async def post_items(item: items):
    print(item)
    return item

#manipulando saida como dictionary saida
@app.post("/items2/")
async def post_item2(item2:items):
    item_dict = item2.dict()
    if item2.tax:
        price_with_tax = item2.price + item2.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

#PUT
@app.put("/items1/{item_id}/")
async def create_item(item_id: int, item: items):
    return {"item_id":item_id, **item.dict()}


from typing import Union,Optional

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: items, q: Union[str,None] = None):
    result = {"item_id":item_id, **item.dict()}
    if q:
        result.update({"q":q})
    return result
