from fastapi import FastAPI, Path

# Создаем экземпляр приложения FastAPI
app = FastAPI()

# маршрут к страницам пользователей по id
@app.get("/user/{user_id}")
async def Get_User_Number(user_id: int = Path(ge=1, le=100, description="Enter User ID", example='1')):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# маршрут к страницам пользователей по имени и возрасту
@app.get("/user/{username}/{age}")
async def Get_User_Name_age(
        username: str = Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser'),
        age: int = Path(ge=18, le=120, description="Enter age", example='24')):
    return {"message": f"Hellow {username}, возраст {age} "}
