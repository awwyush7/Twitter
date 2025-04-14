from fastapi import FastAPI
from backend.servers import authentication_server, tweet_server, user_server  # Changed back to absolute imports

app = FastAPI()

app.include_router(authentication_server.router)
app.include_router(user_server.router)
app.include_router(tweet_server.router)

print("Starting FastAPI server...")