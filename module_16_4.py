from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List
from typing import Annotated

# Создаем экземпляр приложения FastAPI
app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def post_users(
        username: str = Path(min_length=5, max_length=20, description='Enter Username', example='UrbanUser'),
        age: int = Path(ge=18, le=120, description='Enter Age', example='24')):
    user_id = (users[-1].id + 1) if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str = Path(min_length=5, max_length=20, description='Enter Username',
                                                         example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description='Enter Age', example='24')):
    try:
        user = next(user for user in users if user.id == user_id)
        user.username = username
        user.age = age
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail='User was not found')
