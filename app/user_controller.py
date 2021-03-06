from flask import Blueprint, render_template
import database
import json
from flask import jsonify
from flask_login import current_user
from .models import DBSession, User

user = Blueprint('user', __name__)

@user.route("/<username>", methods=['GET'])
def show_user(username):
  try:
    with DBSession() as session:
      user = session.query(User).filter(User.username == username).first()
    if not user:
      return render_template('404.html'), 404

    return render_template("user.html", user=user)
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500

@user.route("/<username>/history", methods=['GET'])
def show_user_history(username):
  if not current_user.is_authenticated:
    return render_template("404.html"), 404

  try:
    user_data = [update.toDict() for update in database.get_user_updates(username)]
    return render_template("history.html", username=username, data=json.dumps(user_data))
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500
