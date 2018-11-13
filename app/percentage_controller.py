from flask import Blueprint, request
import maya
import cgi
import database

percentage = Blueprint('percentage', __name__)

@percentage.route("/percentage", methods=['POST'])
def percentage_update():
  data = request.get_json()
  username = cgi.escape(data["username"])
  try:
    percentage = int(data["percentage"])
    if percentage < 0 or percentage > 100 or len(username) > 16:
      return "Reported percentage out of bounds", 400

    charging = bool(data["charging"])
    updated_at = maya.now().datetime(to_timezone='US/Eastern')

    database.insert_update(username, percentage, charging, updated_at)

    return "Success", 200
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500