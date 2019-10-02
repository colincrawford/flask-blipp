from flask_blipp.flask_blipp import flask_blipp
from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():
        pass

    @app.route("/a", methods=["GET", "PUT"])
    def a():
        pass

    flask_blipp(app)
