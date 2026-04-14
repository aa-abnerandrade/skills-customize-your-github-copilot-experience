from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# TODO: Complete this FastAPI application following the assignment requirements

app = FastAPI()

# TODO: Define the Task model using Pydantic
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False


# TODO: Create an in-memory storage for tasks
tasks: List[Task] = []


# TODO: Implement the GET / endpoint that returns a welcome message
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à minha API!"}


# TODO: Implement the GET /tasks endpoint that returns all tasks
@app.get("/tasks")
def get_tasks():
    pass


# TODO: Implement the POST /tasks endpoint that creates a new task
@app.post("/tasks")
def create_task(task: Task):
    pass


# TODO: Implement the GET /tasks/{task_id} endpoint that returns a specific task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


# TODO: Implement the PUT /tasks/{task_id} endpoint that updates a task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    pass


# TODO: Implement the DELETE /tasks/{task_id} endpoint that deletes a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass


# Run with: uvicorn main:app --reload
