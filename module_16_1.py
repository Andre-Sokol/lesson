from fastapi import FastAPI
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def Get_Main_Page():
    return {"message": "Главная страница"}

# маршрут к странице администратора
@app.get("/user/admin")
async def Get_admin_Ppage():
    return {"message": "Вы вошли как администратор."}

# маршрут к страницам пользователей
@app.get("/user/{user_id}")
async def Get_User_Number(user_id):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# маршрут к страницам пользователей передавая данные в адресной строке
@app.get("/user")
async def Get_User_Info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}



