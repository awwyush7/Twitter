from datetime import datetime
from uuid import UUID
from backend.models.tweet import Tweet
from backend.services.db_services.tweet_service_db import TweetServiceDB
from backend.services.user_service import UserService

class TweetService() :
    # Managment of users
    def __init__(self) :
        self.db_service = TweetServiceDB()
        self.uuid_generator = UUID()   
        self.user_service = UserService()

    def get_id(self) -> str :
        uuid_generator = self.uuid_generator
        id = uuid_generator.uuid4()
        return id
    
    def get_current_user_id(self) -> dict :
        user_service = self.user_service
        current_user =  user_service.get_current_user()
        return current_user["user_id"]
    
    async def add(self,content : str) :
        id = self.get_id()
        current_user_id = self.get_current_user_id()
        tweet = Tweet(id=id, user_id = current_user_id, content=content, date_created=datetime.now())
        db_service = self.db_service
        db_service.add(tweet)
    
    async def get_tweets(self,user_id) -> dict :
        return await self.db_service.get_tweets(user_id)
    
    async def like_tweet(self,tweet_id) -> dict :
        await self.db_service.like_tweet(tweet_id)
    
    async def delete_database(self) :
        collection = self.collection
        await collection.drop()
        return "Database deleted"