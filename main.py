import uvicorn

from enum import Enum
from typing import Union

from fastapi import FastAPI


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    """
    Returns a welcome message for the API.

    Returns:
        A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None): # python3.10 and above: async def read_item(item_id: str, q: str | None = None):
    """
    Returns the details of a specific item.

    Args:
        item_id: A string representing the ID of an item.
        q: A string that represents an optional query parameter.

    Returns:
        A dictionary containing the ID of the item.
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    """
    Returns the details of the current user.

    Returns:
        A dictionary containing the ID of the current user.
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """
    Returns the details of a specific user.

    Args:
        user_id: A string representing the ID of the user to retrieve.

    Returns:
        A dictionary containing the ID of the user.
    """
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Returns a message about the specified model.

    Args:
        model_name: A value from the ModelName enumeration representing the name of the model.

    Returns:
        A dictionary containing a message about the specified model.
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 