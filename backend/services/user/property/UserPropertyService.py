from backend.services.db_services.user_property_db.IUserPropertyServiceDB import IUserPropertyServiceDB
from backend.services.user.property.IUserPropertyService import IUserPropertyService

class UserPropertyService(IUserPropertyService) :
    def __init__(self,db_service : IUserPropertyServiceDB):
        self.db_service = db_service

    async def follow(self, username: str, to_follow: str):
        await self.db_service.follow(username,to_follow)

    async def update_bio(self, username: str, content: str):
        await self.db_service.update_bio(username,content)

    async def delete_database(self):
        await self.db_service.delete_database()

    async def add_follower(self, username: str, follower: str) -> str:
        await self.db_service.add_follower(username,follower)

    async def remove_follow(self, username: str, to_unfollow: str) -> str:
        await self.db_service.remove_follow(username,to_unfollow)

    async def removes_follower(self, username: str, follower: str) -> str:
        await self.db_service.removes_follower(username,follower)
