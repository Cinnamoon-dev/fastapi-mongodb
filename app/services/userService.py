from typing import Any
from bson import ObjectId
from fastapi import HTTPException

from app.models.userModel import User
from app.database import users_collection
from app.database.serializers import document_serial, list_documents

class UserService:
    def get_all_users(self) -> list[dict[str, Any]]:
        # TODO
        # pagination
        return list_documents(list(users_collection.find()))
    
    def view_one_user(self, id: str) -> dict[str, Any]:
        user = users_collection.find_one({"_id": ObjectId(id)})

        if not user:
            raise HTTPException(status_code=404, detail=f"user {id} not found")
        
        return document_serial(user)
    
    def add_user(self, user: User) -> str:
        # TODO
        # add not repeat test case
        new_user = user.model_dump()
        new_user["user_type_id"] = ObjectId(new_user["user_type_id"])
        
        inserted_user_result = users_collection.insert_one(new_user)
        return inserted_user_result.inserted_id
    
    def edit_user(self, id: str, fields: dict[str, Any]) -> str:
        # TODO
        # extract in a method
        document_to_update = users_collection.find_one({"_id": ObjectId(id)})

        if not document_to_update:
            raise HTTPException(status_code=404, detail=f"user {id} not found")

        document_to_update = document_serial(document_to_update)

        fields_dict = dict(fields)
        keys = []

        for k in fields_dict.keys():
            if not fields_dict[k]:
                keys.append(k)
        
        for key in keys:
            fields_dict.pop(key)

        for k, v in fields_dict.items():
            document_to_update[k] = v

        edited_document = users_collection.update_one({"_id": ObjectId(id)}, {"$set": document_to_update})
        return edited_document.upserted_id
    
    def delete_user(self, id: str) -> str:
        deleted_document = users_collection.find_one_and_delete({"_id": ObjectId(id)})

        if deleted_document is None:
            raise HTTPException(status_code=404, detail=f"user {id} not found")

        return dict(deleted_document)["_id"]
