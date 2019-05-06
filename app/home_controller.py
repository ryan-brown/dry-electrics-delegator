from flask import render_template, Blueprint
from flask_login import login_required
from qq import get_shitposts

home = Blueprint('home', __name__)

@home.route("/")
def homepage():
  try:
    return render_template("home.html", shitposts=get_shitposts())
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500

@home.route("/settings", methods=['GET'])
@login_required
def show_settings():
  return render_template("settings.html")


@home.route("/privacy-policy")
def policy():
  return render_template("privacy.html")
