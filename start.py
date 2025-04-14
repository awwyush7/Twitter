import uvicorn
import argparse

def start_user_service() :
    parser = argparse.ArgumentParser(description="MONGODB RESTful API server.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to listen for user service")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen for user services")

    args = parser.parse_args()

    uvicorn.run( 
        "backend.main:app",  
        host=args.host,
        port=args.port,
        timeout_keep_alive=5,
        reload=True,
    )

if __name__ == "__main__":
    start_user_service()
    # .venv\Scripts\activate
    # python -m start