from flask import Flask

from .base_controller import base
from .home_controller import home
from .percentage_controller import percentage
from .user_controller import user
from .stats_controller import stats
from .api_controller import api
from .auth_controller import auth
from .models import User, DBSession
import os

from flask_login import LoginManager

def create_app():
  app = Flask(__name__, instance_relative_config=True)

  app.config['SECRET_KEY'] = os.environ['FLASK_SECRET']

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(user_id):
    with DBSession() as session:
      return session.query(User).filter(User.id == user_id).first()

  app.register_blueprint(base)
  app.register_blueprint(home)
  app.register_blueprint(percentage)
  app.register_blueprint(auth)
  app.register_blueprint(stats, url_prefix='/stats')
  app.register_blueprint(api, url_prefix='/api')
  app.register_blueprint(user, url_prefix='/users')

  return app
