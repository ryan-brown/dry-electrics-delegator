from flask import Blueprint, render_template
import database
import json
from flask import jsonify

from .home_controller import get_leaderboard

user = Blueprint('user', __name__)

@user.route("/driest", methods=['GET', 'POST'])
def driest():
    all_users = get_leaderboard()
    if len(all_users) < 1:
        return "No data", 204
    
    lowest = all_users[0]
    print(lowest)
    return jsonify({"payload": {
        "google": {
        "expectUserResponse": False,
        "richResponse": {
        "items": [
        {
        "simpleResponse": {
        "textToSpeech": "%s at %d percent" % (lowest[1], lowest[2])
        }
        }
        ]
        }
        }}})

@user.route("/<username>", methods=['GET'])
def show_user(username):
  try:
    user_data = [[d[2], d[3], str(d[4])] for d in database.get_user_data(username)]
    return render_template("user.html", username=username, data=json.dumps(user_data))
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500



