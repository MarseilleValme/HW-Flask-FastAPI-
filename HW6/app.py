# Задание №3
# 📌 Создать API для управления списком задач.
# 📌 Каждая задача должна содержать поля "название", "описание" и "статус" (выполнена/не выполнена).
# 📌 API должен позволять выполнять CRUD операции с задачами.
# Задание №4
# 📌 Напишите API для управления списком задач. Для этого создайте модель Task со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)

from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///database_hw06.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(30)),
    sqlalchemy.Column("description", sqlalchemy.String(160)),
    sqlalchemy.Column("done", sqlalchemy.Boolean()),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


class TaskIn(BaseModel):
    title: str = Field(..., max_length=30)
    description: str = Field(..., max_length=160)
    done: bool = Field(default=False)


class Task(TaskIn):
    id: int


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    return {**task.model_dump(), "id": last_record_id}


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.model_dump())
    await database.execute(query)
    return {**new_task.model_dump(), "id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'task deleted'}