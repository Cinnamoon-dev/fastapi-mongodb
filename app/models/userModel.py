from bson import ObjectId
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    user_type_id: ObjectId