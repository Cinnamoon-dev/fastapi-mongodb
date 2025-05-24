from typing import Optional
from pydantic import BaseModel, EmailStr


class UserAddSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    user_type_id: str

class UserEditSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    user_type_id: Optional[str] = None