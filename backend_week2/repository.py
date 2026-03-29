from schemas import UserUpdate
import uuid

_users = {}

def create_user(name: str, email: str) -> dict:
    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "name": name,
        "email": email
    }
    _users[user_id] = user
    return user

def get_user_by_id(user_id: str) -> dict | None:
    return _users.get(user_id)

def get_user_by_email(email: str) -> dict | None:
    for user in _users.values():
        if user["email"] == email:
            return user
    return None

def update_user(id: str, update: UserUpdate) -> dict:
    user.name= update.name
    user.email= update.email
