from abc import ABC, abstractmethod

class IUserServiceDB(ABC):
    @abstractmethod
    async def add(self,tweet):
        pass
    @abstractmethod
    async def get_tweets(self,user_id) :
        pass
    @abstractmethod
    async def like_tweet(elf,tweet_id):
        pass
    @abstractmethod
    async def delete_database(self) :
        pass
