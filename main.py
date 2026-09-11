from fastapi import FastAPI
from pydantic import BaseModel
# from CRUD import router as todo_router
from test import router as test_router
from controller.CRUD import router as todo_router

app = FastAPI()
app.include_router(todo_router)
app.include_router(test_router)


#Normal get API
@app.get("/list")
def home():
    return {
        "data":[
            {
                "id":1,
                "name":"John Doe",
                "email":"z5AqM@example.com"
            },
            {
                "id":2,
                "name":"Jane Doe",
                "email":"awd@`example.com"
            }
        ]
    }

# API using path parameter
@app.get("/user/{id}")
def get_user_by_id(id :int):
    return {
        "data":{
            "id":id,
            "name":"John Doe",
            "email":"z5AqM@example.com"
        },
        "isSuccess": True
    }

# API using query parameter
@app.get("/user")
def get_user_by_query_param(
    name: str = None,
    email: str = None,
    page: int = 0,
    size: int = 10
):
    users = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "z5AqM@example.com"
        },
        {
            "id": 2,
            "name": "Jo Doe",
            "email": "awd@example.com"
        }
    ]

    matching_users = []

    # Search
    for user in users:
        if name and name.lower() in user["name"].lower():
            matching_users.append(user)

        elif email and email.lower() in user["email"].lower():
            matching_users.append(user)

    # Use search results if search parameter is provided
    if name or email:
        if not matching_users:
            return []

        users = matching_users

    # Pagination
    start = page * size
    end = start + size

    paginated_users = users[start:end]

    return {
        "data": paginated_users,
        "isSuccess": True,
        "page": page,
        "size": size,
        "total": len(paginated_users)
    }


#POST API 
class User(BaseModel):
    name: str
    email: str
    age: None|int
    address: Address

class Address(BaseModel):
    line1: str
    street: str
    city: str
    state: str
    zip_code: str

@app.post("/create-user")
def create_user(user: User):
    return {
        "data": user,
        "isSuccess": True,
        "message": "User created successfully"
    }

@app.post("/save-user")
def save_user(user: User):
    return {
        "data": user,
        "isSuccess": True,
        "message": "User saved successfully"
    }