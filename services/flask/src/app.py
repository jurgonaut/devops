from flask import Flask, session
import os


def create_app():
    app = Flask(__name__)

    from routes import route_blueprint
    app.register_blueprint(route_blueprint)

    app.config["NAME"] = os.environ.get("NAME", "app")

    return app


# When running with Gunicorn
app = create_app()

# When running in dev mode
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    app.run(host=host, port=port, debug=True)
