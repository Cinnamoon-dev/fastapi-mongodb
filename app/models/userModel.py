from bson import ObjectId
from pydantic import BaseModel, EmailStr, model_validator


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    user_type_id: str

    @model_validator(mode="after")
    def validate_user_type_id(self):
        if not ObjectId.is_valid(self.user_type_id):
            raise ValueError("Invalid user_type_id!")

        return self
