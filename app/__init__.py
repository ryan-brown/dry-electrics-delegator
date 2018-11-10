from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app