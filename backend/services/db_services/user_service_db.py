from backend.models.user import UserInput
from motor.motor_asyncio import AsyncIOMotorClient

from backend.services.password_managment import PasswordManagment

class UserServiceDB() :
    # Managment of users
    def __init__(self) :
        self.total_users = 0
        self.client = AsyncIOMotorClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.4")
        self.database = self.client["Twitters"]
        self.collection = self.database["Users"]
        self.password_manager = PasswordManagment()

    def serialize_user(self,user):
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return user

    def get_hashed_password(self,password) :
        return self.password_manager.hash_password(password)
    
    async def add(self,user : UserInput) :
        user_document = user.model_dump()
        total_users = self.total_users
        user_document["password"] = self.get_hashed_password(user_document["password"])
        user_document["user_id"] = total_users+1
        self.total_users += 1
        collection = self.collection
        add_result = await collection.insert_one(user_document)
        return add_result
    
    async def get_all(self) : 
        collection = self.collection
        users_list = []
        users_cursor = collection.find()
        async for user in  users_cursor : 
            users_list.append(user)
        return users_list
    
    async def get_user(self,username) -> dict :
        collection = self.collection
        fetched_user = await collection.find_one({"username" : username})
        if fetched_user:
            user = self.serialize_user(fetched_user)
        return user

    async def delete_database(self) :
        collection = self.collection
        await collection.drop()
        return "Database deleted"