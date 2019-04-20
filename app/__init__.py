from flask import Flask

from .base_controller import base
from .home_controller import home
from .percentage_controller import percentage
from .user_controller import user
from .stats_controller import stats
from .api_controller import api
from .vr_graphs_controller import vr_graphs


def create_app():
  app = Flask(__name__, instance_relative_config=True)

  app.register_blueprint(base)
  app.register_blueprint(home)
  app.register_blueprint(percentage)
  app.register_blueprint(stats, url_prefix='/stats')
  app.register_blueprint(api, url_prefix='/api')
  app.register_blueprint(user, url_prefix='/users')
  app.register_blueprint(vr_graphs, url_prefix='/vr_graphs')

  return app
