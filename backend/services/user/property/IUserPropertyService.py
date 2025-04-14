from abc import ABC, abstractmethod

class IUserPropertyService(ABC):
    @abstractmethod
    async def follow(self,username : str, to_follow : str):
        pass
    @abstractmethod
    async def update_bio(self,content) :
        pass
    @abstractmethod
    async def delete_database(self) :
        pass
    @abstractmethod
    async def add_follower(self,username : str, follower : str) -> str:
        pass
    @abstractmethod
    async def remove_follow(self,username : str, to_unfollow : str) -> str:
        pass
    @abstractmethod
    async def removes_follower(self,username : str, follower : str) -> str:
        pass
