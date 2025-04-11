from fastapi import FastAPI
from backend.services.tweet.tweet_service import TweetService

app = FastAPI()

@app.get("/health")
def health() :
    return "Ok"

@app.post("/create_tweet")
async def add(content : str) :
    tweet_service = TweetService()
    tweet = tweet_service.add(content)
    return "Tweet Created"
