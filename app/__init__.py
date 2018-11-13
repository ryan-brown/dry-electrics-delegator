from flask import Flask

from .base_controller import base
from .home_controller import home
from .percentage_controller import percentage
from .user_controller import user

def create_app():
  app = Flask(__name__, instance_relative_config=True)

  app.register_blueprint(base)
  app.register_blueprint(home)
  app.register_blueprint(percentage)
  app.register_blueprint(user, url_prefix='/users')

  return app
