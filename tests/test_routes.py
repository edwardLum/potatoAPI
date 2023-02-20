from enum import Enum

from fastapi.testclient import TestClient

from potatoAPI.main import app


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_item():
    client = TestClient(app)
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": "1"}

    response = client.get("/items/1?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": "1", "q": "test"}


def test_read_user_me():
    client = TestClient(app)
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"user_id": "the current user"}


def test_read_user():
    client = TestClient(app)
    response = client.get("/users/123")
    assert response.status_code == 200
    assert response.json() == {"user_id": "123"}


def test_get_model():
    client = TestClient(app)
    response = client.get("/models/alexnet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "alexnet", "message": "Deep Learning FTW"}

    response = client.get("/models/lenet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "lenet", "message": "LeCNN all the images"}

    response = client.get("/models/resnet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "resnet", "message": "Have some residuals"}

    response = client.get("/models/xxxxxx")  # item with ID 999 doesn't exist
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["path","model_name"],"msg":"value is not a valid enumeration member; permitted: 'alexnet', 'resnet', 'lenet'","type":"type_error.enum","ctx":{"enum_values":["alexnet","resnet","lenet"]}}]}
