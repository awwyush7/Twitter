import uvicorn
import argparse

def start_tweet_service() :
    parser = argparse.ArgumentParser(description="MONGODB RESTful API server.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to listen for tweet service")
    parser.add_argument("--port", type=int, default=4453, help="Port to listen for tweet services")

    args = parser.parse_args()

    uvicorn.run( 
        "backend.servers.tweet_server:app", 
        host=args.host,
        port=args.port,
        timeout_keep_alive=5,
        reload=True,
    )    

if __name__ == "__main__":
    start_tweet_service()


    # .venv\Scripts\activate
    # python -m start_tweet_service