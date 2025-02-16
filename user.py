from fastapi import APIRouter
router = APIRouter()

users = {}

# basic CRUD functions
@router.post("/user/")
def create_user(user_id: int, username: str, phone: str, email: str):
    users[user_id] = {"username": username, "phone": phone, "email": email}
    return {"message": "User created successfully"}

@router.get("/user/{user_id}")
def find_user(user_id: int):
    return users.get(user_id, {"error" : "Could not find user"})

@router.put("/user/{user_id}")
def update_user(user_id: int, username: str, phone: str, email: str):
    if user_id in users:
        users[user_id]["username"] = username
        users[user_id]["phone"] = phone
        users[user_id]["email"] = email
        return {"message": "Updated user"}
    return {"message": "User not found"}

@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    return users.pop(user_id, {"error": "Could not find user"})