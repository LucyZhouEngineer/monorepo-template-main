from fastapi.testclient import TestClient
from src.main import app, User


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_user():
    user_id = 1
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"user_id": user_id}


def test_search_user():
    username = "testuser"
    response = client.get(f"/search/?username={username}")
    assert response.status_code == 200
    assert response.json() == {"username": username}


def test_create_user():
    user_data = {"username": "test", "email": "test@example.com", "age": 25}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data
