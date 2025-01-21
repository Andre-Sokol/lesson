from fastapi import FastAPI, Path

# Создаем экземпляр приложения FastAPI
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_users(
        username: str = Path(min_length=5, max_length=20, description='Enter Username', example='UrbanUser'),
        age: int = Path(ge=18, le=120, description='Enter Age', example='24')):
    current_index = str(int(max(users, key=int)) + 1)
    user = f'Имя: {username}, возраст: {age}'
    users[current_index] = user
    return current_index


@app.put("/user/{user_id}")
async def update_user(user_id: int, username: str = Path(min_length=5, max_length=20, description='Enter Username',
                                                         example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description='Enter Age', example='24')):
    try:
        user = (user for user in users if user.id == user_id)
        user.username = username
        user.age = age
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(min_length=1, max_length=1000, description='Enter User ID')) -> str:
    try:
        users.pop(user_id)
        return f"User id = {user_id} deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
