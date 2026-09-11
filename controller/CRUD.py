from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# Create a model for todos
class TODO(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# Create a todo list
todos = []

# Create a todo
@router.post("/todo")
def create_todo(todo: TODO):
    todos.append(todo)
    return {
        "data": todo,
        "message": "Todo created successfully",
        "isSuccess": True
    }

# Get all todos
@router.get("/todo")
def get_todos():
    return {
        "data": todos,
        "message": "Todos fetched successfully",
        "isSuccess": True
    }

# Get todo by ID
@router.get("/todo/{id}")
def get_todo_by_id(id: int):
    for todo in todos:
        if todo.id == id:
            return {
                "data": todo,
                "message": "Todo fetched successfully",
                "isSuccess": True
            }
    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# Update todo by ID
@router.put("/todo/{id}")
def update_todo(id: int, updated_todo: TODO):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = updated_todo
            return {
                "data": updated_todo,
                "message": "Todo updated successfully",
                "isSuccess": True
            }
    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# Delete todo by ID
@router.delete("/todo/{id}")
def delete_todo(id: int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            deleted_todo = todos.pop(index)
            return {
                "data": deleted_todo,
                "message": "Todo deleted successfully",
                "isSuccess": True
            }
    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )