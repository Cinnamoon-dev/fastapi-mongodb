from fastapi import APIRouter

from app.models.userModel import User
from app.adapters.userAdapter import UserAdapter
from app.schemas.userSchema import UserEditSchema

router = APIRouter(prefix="/user")


@router.get("/all")
async def user_all():
    return UserAdapter().user_all_controller()

@router.get("/view/{id}")
async def user_view(id):
    return UserAdapter().user_view_controller(id)

@router.post("/add")
async def user_add(user: User):
    return UserAdapter().user_add_controller(user)

@router.put("/edit/{id}")
async def user_edit(id: str, user: UserEditSchema):
    return UserAdapter().user_edit_controller(id, user)

@router.delete("/delete/{id}")
async def user_delete(id: str):
    return UserAdapter().user_delete_controller(id)