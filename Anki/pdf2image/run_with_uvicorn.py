from uvicorn.middleware.wsgi import WSGIMiddleware
from uvicorn import Config, Server
from main import app  # Import your Flask app

if __name__ == "__main__":
    # Wrap Flask app with WSGIMiddleware
    asgi_app = WSGIMiddleware(app)

    # Run the server
    server = Server(Config(app=asgi_app, host="localhost", port=8000))
    server.run()
