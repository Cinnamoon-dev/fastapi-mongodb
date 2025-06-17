from fastapi import HTTPException

from app.models.userModel import User
from app.services.userService import UserService
from app.schemas.userSchema import UserAddSchema, UserEditSchema


class UserAdapter:
    async def user_all_controller(self):
        users = await UserService().get_all_users()
        return {"error": False, "data": users}

    async def user_view_controller(self, user_id: str):
        user = await UserService().view_one_user(user_id)
        return {"error": False, "data": user}

    async def user_add_controller(self, user: UserAddSchema):
        try:
            new_user = User(
                name=user.name,
                email=user.email,
                password=user.password,
                user_type_id=user.user_type_id,
            )
        except Exception as e:
            raise HTTPException(status_code=422, detail="User body invalid!")

        inserted_id = await UserService().add_user(new_user)
        return {"error": False, "message": f"user {inserted_id} added successfully"}

    async def user_edit_controller(self, user_id: str, fields: UserEditSchema):
        edited_user_id = await UserService().edit_user(user_id, fields.model_dump())
        return {"error": False, "message": f"user {edited_user_id} edited successfully"}

    async def user_delete_controller(self, user_id: str):
        deleted_user_id = await UserService().delete_user(user_id)
        return {
            "error": False,
            "message": f"user {deleted_user_id} deleted successfully",
        }
