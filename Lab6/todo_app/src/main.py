from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    username: str
    email: str
    age: int


# Create a GET ReST API
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Create a GET ReST API with path parameters
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


# Create a GET ReST API with query parameters
@app.get("/search/")
def search_user(username: str = None):
    return {"username": username}


# Create a GET ReST API with path parameters AND query parameters
@app.get("/products/{product_id}")
def read_product(product_id: int, q: str = None):
    return {"product_id": product_id, "query": q}


# Create a POST ReST API
@app.post("/users/")
def create_user(user: User):
    return {"username": user.username, "email": user.email, "age": user.age}


# Create a PUT ReST API
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {
        "user_id": user_id,
        "username": user.username,
        "email": user.email,
        "age": user.age,
    }


# Create a DELETE ReST API
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"status": "success", "message": f"User with id {user_id} has been deleted."}
