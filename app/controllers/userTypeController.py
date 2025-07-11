from fastapi import APIRouter

from app.adapters.userTypeAdapter import UserTypeAdapter
from app.schemas.userTypeSchema import UserTypeEditSchema, UserTypeAddSchema

router = APIRouter(prefix="/user/type", tags=["user type"])


@router.get("/")
async def user_type_all():
    return await UserTypeAdapter().user_type_all_controller()


@router.get("/{id}")
async def user_type_view(id: str):
    return await UserTypeAdapter().user_type_view_controller(id)


@router.get("/name/{name}")
async def user_type_view_by_name(name: str):
    return await UserTypeAdapter().user_type_view_by_name_controller(name)


@router.post("/")
async def user_type_add(user_type: UserTypeAddSchema):
    return await UserTypeAdapter().user_type_add_controller(user_type)


@router.put("/{id}")
async def user_type_edit(id: str, user_type: UserTypeEditSchema):
    return await UserTypeAdapter().user_type_edit_controller(id, user_type)


@router.delete("/{id}")
async def user_type_delete(id: str):
    return await UserTypeAdapter().user_type_delete_controller(id)
