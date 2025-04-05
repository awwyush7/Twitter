from datetime import datetime
from uuid import UUID
from backend.models.tweet import Tweet
from backend.models.user import User
from passlib.context import CryptContext
from motor.motor_asyncio import AsyncIOMotorClient

from backend.services.password_managment import PasswordManagment
from backend.services.tweet_service_db import TweetServiceDB

class TweetService() :
    # Managment of users
    def __init__(self) :
        self.db_service = TweetServiceDB()
        self.uuid_generator = UUID()   
    
    async def add(self,user_id : int,content : str) :
        uuid_generator = self.uuid_generator
        id = uuid_generator.uuid4()
        tweet = Tweet(id=id, user_id=user_id, content=content, date_created=datetime.now())
        db_service = self.db_service
        db_service.add(tweet)
    
    async def get_tweets(self,user_id) -> dict :
        return await self.db_service.get_tweets(user_id)

    async def delete_database(self) :
        collection = self.collection
        await collection.drop()
        return "Database deleted"