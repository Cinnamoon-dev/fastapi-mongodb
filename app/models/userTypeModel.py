from pydantic import BaseModel, model_validator

class UserType(BaseModel):
    name: str

    @model_validator(mode="after")
    def check_name(self):
        if self.name == "":
            raise ValueError("Name field should not be empty!")
        return self