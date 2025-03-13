from fastapi import APIRouter, HTTPException
from schemas import UserCreate, UserResponse
from controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

# Create User
@router.post("/", response_model=UserResponse)
async def create_user(user_data: UserCreate):
    user = await user_controller.create_user(user_data)
    return user

# Get All Users
@router.get("/", response_model=list[UserResponse])
async def get_users():
    return await user_controller.get_users()

# Get User by ID
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = await user_controller.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update User
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserCreate):
    user = await user_controller.update_user(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Delete User
@router.delete("/{user_id}")
async def delete_user(user_id: int):
    deleted = await user_controller.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
