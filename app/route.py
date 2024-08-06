
from flask import Flask, request
from app import scan, select_by_id, insert, update_by_id, delete_by_id

app = Flask(__name__)

@app.get("/tasks")
def get_all_tasks():
    tasks_list = scan()
    out = {
        "tasks": tasks_list,
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>/")
def get_single_task(pk):
    single_task = select_by_id(pk)
    if single_task:
        out = {
            "task": single_task,
            "ok": True
        }
        return out
    out = {
        "ok": False,
        "message": "Not Found"
    }
    return out, 404

@app.post("/tasks")
def create_task():
    task_data = request.json
    insert(task_data)
    return "", 204

@app.put("/tasks/<int:pk>/")
def update_task(pk):
    task_data = request.json
    update_by_id(task_data, pk)
    return "", 204

@app.delete("/tasks/<int:pk>/")
def delete_task(pk):
    delete_by_id(pk)
    return "", 204
