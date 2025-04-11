from abc import ABC, abstractmethod

class IUserService(ABC):
    @abstractmethod
    def get_current_user_id(self):
        pass
    @abstractmethod
    async def add(self,content) :
        pass
    @abstractmethod
    async def get_tweets(self,user_id):
        pass
    @abstractmethod
    async def like_tweet(self,tweet_id) :
        pass
    @abstractmethod
    async def delete_database(self) :
        pass

