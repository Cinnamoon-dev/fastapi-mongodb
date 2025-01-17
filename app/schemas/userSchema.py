from typing import Optional
from pydantic import BaseModel

class UserEditSchema(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None