# Задание №3
# 📌 Создать API для добавления нового пользователя в базу данных. Приложение должно иметь возможность принимать POST
# запросы с данными нового пользователя и сохранять их в базу данных.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте маршрут для добавления нового пользователя (метод POST).
# 📌 Реализуйте валидацию данных запроса и ответа.
# Задание №4
# 📌 Приложение должно иметь возможность принимать PUT запросы с данными пользователей и обновлять их в базе данных.
# 📌 Создайте маршрут для обновления информации о пользователе (метод PUT).
# Задание №5
# 📌 Создать API для удаления информации о пользователе из базы данных. Приложение должно иметь возможность принимать
# DELETE запросы и удалять информацию о пользователе из базы данных.
# 📌 Создайте маршрут для удаления информации о пользователе (метод DELETE).
# 📌 Реализуйте проверку наличия пользователя в списке и удаление его из списка.
# Задание №6
# 📌 Создать веб-страницу для отображения списка пользователей. Приложение должно использовать шаблонизатор Jinja
# для динамического формирования HTML страницы.
# 📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен содержать заголовок страницы, таблицу со
# списком пользователей и кнопку для добавления нового пользователя.
# 📌 Создайте маршрут для отображения списка пользователей (метод GET).
# 📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []
for i in range(10):
    new_user = User(id=i, name=f'User {i + 1}', email=f'user{i + 1}@mail.ru', password=f'user{i + 1}')
    users.append(new_user)


@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", {"request": request, 'title': 'Главная'})


@app.post("/users/")
async def add_user(user: User):
    users.append(user)
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u = user
    return user


@app.delete("//users/{user_id}")
async def delete_user(user_id: int):
    if user_id <= len(users):
        return {"User delete": users.pop(user_id)}
    return HTTPException(status_code=404, detail='User not found')


@app.get("/users/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, 'users': users, 'title': 'Пользователи'})