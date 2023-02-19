from enum import Enum

from fastapi import FastAPI


app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lesnet"


@app.get("/")
async def root():
    """
    Returns a welcome message for the API.

    Returns:
        A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Returns the details of a specific item.

    Args:
        item_id: An integer representing the ID of the item to retrieve.

    Returns:
        A dictionary containing the ID of the item.
    """
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


@app.get("files/{file_path:path}")
async def read_file(file_path: str):
    """
    Returns the contents of the specified file.

    Args:
        file_path: A string representing the path to the file.

    Returns:
        A dictionary containing the contents of the specified file.
    """
    return {"file_path": file_path}
