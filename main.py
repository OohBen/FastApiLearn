# from typing import Annotated
# from fastapi import FastAPI, Query, Path
# from enum import Enum

# from pydantic import BaseModel, Required
# app = FastAPI()

# class ModelName(str,Enum):
#     alexnet='alexnet'
#     resnet='resnet'
#     lenet='lenet'


# @app.get("/")
# def root():
#     return {"message": "aye nice"}


# @app.get("/posts/")

# def get_posts():
#     return {"data":"hella posts"}


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     return {"enumtest":ModelName(model_name)}

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# # @app.post("/items/")
# # async def create_item(item: Item):
# #     item_dct = item.dict()
# #     if item.tax:
# #         price_with_tax = item.price + item.price*item.tax
# #         item_dct.update({"price_with_tax":price_with_tax})
# #     return item_dct
# # @app.put("/items/{item_id}")
# async def make_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# # @app.get("/items/{item_id}") 
# # async def read_item(item_id: str, q:str | None = None): #item id a path parameter while q is query parameter fastapi auto figures it out (:
# #     if q:
# #         return {"item_id": item_id, "q":q}
# #     else:
# #         return {"item_id": item_id}

# # @app.get("/items/")
# # async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
# #     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
# #     if q:
# #         results.update({"q": q})
# #     return results

# # @app.get("/items/") 
# # async def read_items(q: Annotated[str | None, Query(min_length=3)] = Required)  #Either use ... or Required for required values that can be emptyThis means the person has to send soemtihng even if it is None
# #     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
# #     if q:
# #         results.update({"q": q})
# #     return results

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get",ge=1,le=12)], #greater than or equal to 1 less than or equal to 12, gt and lt for greater than and less then not equal to
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

from typing import Annotated

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str | None = None,
#     item: Item | None = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results
@app.put("/items/{item_id}")
async def update_item(item_id: Annotated[int, Path(ge=1)], item: Item, user: User, importnace: Annotated[str, Body()]):
    results = {"item_id": item_id, "item": item, "user": user}
    return results
