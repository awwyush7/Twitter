import uvicorn
import argparse

def start_authentication_service() :
    parser = argparse.ArgumentParser(description="MONGODB RESTful API server.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to listen for user service")
    parser.add_argument("--port", type=int, default=8080, help="Port to listen for user services")

    args = parser.parse_args()

    uvicorn.run( 
        "backend.servers.authentication_server:app",  
        host=args.host,
        port=args.port,
        timeout_keep_alive=5,
        reload=True,
    )

if __name__ == "__main__":
    start_authentication_service()
    # .venv\Scripts\activate
    # python -m start_authentication_service