from backend.models.tweet import Tweet
from motor.motor_asyncio import AsyncIOMotorClient

class TweetServiceDB() :
    # Managment of users
    def __init__(self) :
        self.client = AsyncIOMotorClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.4")
        self.database = self.client["Twitters"]
        self.collection = self.database["Tweets"]
    
    async def add(self,tweet : Tweet) :
        collection = self.collection
        tweet_document = tweet.model_dump()
        add_result = await collection.insert_one(tweet_document)
        return add_result

    async def get_tweets(self,user_id) -> dict :
        collection = self.collection
        fetched_tweets = await collection.find({"user_id" : user_id})
        tweets = []
        async for tweet in fetched_tweets :
            tweets.append(tweet)
        return tweets
    
    async def like_tweet(self,tweet_id) -> dict :
        collection = self.collection
        tweet = await collection.find_one({"id" : tweet_id})
        tweet_likes = tweet["likes"]
        await collection.update_one({"id" : tweet_id},{"$set" : {"likes" : tweet_likes + 1}})

    async def delete_database(self) :
        collection = self.collection
        await collection.drop()
        return "Database deleted"