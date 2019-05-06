from flask import Blueprint, request
import maya
import cgi
import qq
from .models import User, Update, DBSession

percentage = Blueprint('percentage', __name__)

@percentage.route("/percentage", methods=['POST'])
def percentage_update():
  data = request.get_json()
  zap_token = data["zap_token"]

  try:
    percentage = int(data["percentage"])
    if percentage < 0 or percentage > 100:
      return "Reported percentage out of bounds", 400

    charging = bool(data["charging"])
    updated_at = maya.now().datetime(to_timezone='US/Eastern')

    with DBSession() as session:
      user = session.query(User).filter(User.zap_token == zap_token).first()

    if not user:
      return "Zap token not recognized", 401

    new_update = Update(user_id=user.id, percentage=percentage, charging=charging, updated_at=updated_at)
    qq.insert_update(new_update, user.username)

    return "Success", 200
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500
