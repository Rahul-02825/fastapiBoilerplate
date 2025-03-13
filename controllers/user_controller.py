from models import User
from schemas import UserCreate

async def create_user(user_data: UserCreate):
    return await User.create(**user_data.dict())

async def get_users():
    return await User.all()

async def get_user(user_id: int):
    return await User.get_or_none(id=user_id)

async def update_user(user_id: int, user_data: UserCreate):
    user = await User.get_or_none(id=user_id)
    if not user:
        return None
    
    await user.update_from_dict(user_data.dict()).save()
    return user

async def delete_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        return None
    
    await user.delete()
    return True
