from fastapi import APIRouter

from app.adapters.userAdapter import UserAdapter
from app.schemas.userSchema import UserEditSchema, UserAddSchema

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/all")
async def user_all():
    return await UserAdapter().user_all_controller()

@router.get("/view/{user_id}")
async def user_view(user_id: str):
    return await UserAdapter().user_view_controller(user_id)

@router.post("/add")
async def user_add(user: UserAddSchema):
    return await UserAdapter().user_add_controller(user)

@router.put("/edit/{user_id}")
async def user_edit(user_id: str, user: UserEditSchema):
    return await UserAdapter().user_edit_controller(user_id, user)

@router.delete("/delete/{user_id}")
async def user_delete(user_id: str):
    return await UserAdapter().user_delete_controller(user_id)