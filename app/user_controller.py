from flask import Blueprint, render_template
import database
import json
from flask import jsonify

user = Blueprint('user', __name__)

@user.route("/<username>", methods=['GET'])
def show_user(username):
  try:
    user_data = [update.toDict() for update in database.get_user_updates(username)]
    return render_template("user.html", username=username, data=json.dumps(user_data))
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500
