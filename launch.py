import uvicorn
import argparse

from main import app
from configs import config

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=config.BASE_URL, help="Host address")
    parser.add_argument("--port", default=config.BASE_PORT, type=int, help="Port number")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    return parser.parse_args()

if __name__ == "__main__":

    args = parse_arguments()

    if args.reload==True:
        uvicorn.run("main:app", host=args.host, port=args.port, reload=args.reload)
    else:
        uvicorn.run(app, host=args.host, port=args.port, reload=False)