from flask import Blueprint, render_template
import database

user = Blueprint('user', __name__)

@user.route("/<username>", methods=['GET'])
def show_user(username):
  try:
    user_data = [d[2:] for d in database.get_user_data(username)]
    return render_template("user.html", username=username, data=user_data)
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500