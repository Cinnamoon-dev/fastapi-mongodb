from pydantic import BaseModel


class UserTypeAddSchema(BaseModel):
    name: str

class UserTypeEditSchema(BaseModel):
    name: str