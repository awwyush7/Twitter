from fastapi import APIRouter
from backend.services.tweet.TweetService import TweetService

router = APIRouter(prefix="/tweets", tags = ["Tweet"])

@router.get("/health")
def health() :
    return "Ok"

@router.post("/create_tweet")
async def add(content : str) :
    tweet_service = TweetService()
    tweet = tweet_service.add(content)
    return "Tweet Created"
