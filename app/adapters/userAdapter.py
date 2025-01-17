from app.models.userModel import User
from app.services.userService import UserService

class UserAdapter:
    def user_all_controller(self):
        users = UserService().get_all_users()
        return {"error": False, "data": users}
    
    def user_view_controller(self, id):
        user = UserService().view_one_user(id)
        return {"error": False, "data": user}
    
    def user_add_controller(self, user: User):
        inserterd_id = UserService().add_user(user)
        return {"error": False, "message": f"user {inserterd_id} added successfully"}
    
    def user_edit_controller(self, id, fields):
        edited_id = UserService().edit_user(id, fields)
        return {"error": False, "message": f"user {edited_id} edited successfully"}
    
    def user_delete_controller(self, id):
        deleted_id = UserService().delete_user(id)
        return {"error": False, "message": f"user {deleted_id} deleted successfully"}