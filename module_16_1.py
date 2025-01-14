from fastapi import FastAPI
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def Get_Main_Page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def Get_admin_Ppage():
    return {"message": "Вы вошли как администратор."}

@app.get("/user/{user_id}")
async def Get_User_Number(user_id):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def Get_User_Info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

# @app.get("/user/frist_name/last_name")
# async def new(frist_name: str, last_name: str) -> dict:
#     return {"message": f"Привет, {frist_name} {last_name}"}

