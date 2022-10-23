from flask import Flask

from config import config

# Routes
from routes import Movies

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Not found page</h1>"


if __name__ == "__main__":
    # Debug mode on
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Movies.main, url_prefix='/api/movies')

    # Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
