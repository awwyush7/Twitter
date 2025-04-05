from fastapi import FastAPI
from backend.services.tweet_service import TweetService

app = FastAPI()

@app.get("/health")
def health() :
    return "Ok"

@app.post("/create_tweet")
async def add(user_id : int,content : str) :
    tweet_service = TweetService()
    tweet = tweet_service.add(user_id,content)
    return "Tweet Created"
