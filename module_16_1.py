from fastapi import FastAPI


# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def Get_Main_Page()-> str:
    return "Главная страница"

# маршрут к странице администратора
@app.get("/user/admin")
async def Get_admin_Ppage()-> str:
    return "Вы вошли как администратор."

# маршрут к страницам пользователей
@app.get("/user/{user_id}")
async def Get_User_Number(user_id):
    return f"Вы вошли как пользователь № {user_id}"

# маршрут к страницам пользователей передавая данные в адресной строке
@app.get("/user")
async def Get_User_Info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"



