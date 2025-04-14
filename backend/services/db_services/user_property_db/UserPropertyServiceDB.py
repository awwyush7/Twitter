from backend.services.db_services.user_property_db.IUserPropertyServiceDB import IUserPropertyServiceDB
from motor.motor_asyncio import AsyncIOMotorClient

class UserPropertyServiceDB(IUserPropertyServiceDB) :
    def __init__(self):
        self.client = AsyncIOMotorClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.4")
        self.database = self.client["Twitters"]
        self.collection = self.database["UserProperties"]

    async def follow(self, username: str, to_follow: str):
        await self.collection.update_one(
            {"username": username},
            {"$addToSet": {"following": to_follow}, "$inc": {"total_following": 1}}
        )
        await self.add_follower(to_follow, username)

    async def update_bio(self, username: str, content: str):
        await self.collection.update_one(
            {"username": username},
            {"$set": {"bio": content}}
        )

    async def delete_database(self):
        await self.collection.drop()

    async def add_follower(self, username: str, follower: str) -> str:
        await self.collection.update_one(
            {"username": username},
            {"$addToSet": {"followers": follower}, "$inc": {"total_followers": 1}}
        )
        return f"{follower} added as a follower to {username}"

    async def remove_follow(self, username: str, to_unfollow: str) -> str:
        await self.collection.update_one(
            {"username": username},
            {"$pull": {"following": to_unfollow}, "$inc": {"total_following": -1}}
        )
        await self.removes_follower(to_unfollow, username)
        return f"{username} unfollowed {to_unfollow}"

    async def removes_follower(self, username: str, follower: str) -> str:
        await self.collection.update_one(
            {"username": username},
            {"$pull": {"followers": follower}, "$inc": {"total_followers": -1}}
        )
        return f"{follower} removed as a follower from {username}"

