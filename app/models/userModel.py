from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    course: str

def user_serial(user: User):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "age": user["age"],
        "course": user["course"]
    }

def list_users(users):
    return [user_serial(user) for user in users]