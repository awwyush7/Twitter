import uvicorn
import argparse



def start_tweet_service() :
    parser = argparse.ArgumentParser(description="MONGODB RESTful API server.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to listen for tweet service")
    parser.add_argument("--port", type=int, default=4453, help="Port to listen for tweet services")

    args = parser.parse_args()

    uvicorn.run( 
        "backend.tweet_server:app",  # Corrected module path
        host=args.host,
        port=args.port,
        timeout_keep_alive=5,
        reload=True,
    )    

if __name__ == "__main__":
    # Uncomment the service you want to run
    start_tweet_service()
    # To run the server, use the command below in the terminal:
    # .venv\Scripts\activate
    # python -m backend.server