from flask import render_template, Blueprint
import database
import os

from .api_controller import get_leaderboard

home = Blueprint('home', __name__)

@home.route("/")
def homepage():
  try:
    leaderboard_rows = get_leaderboard()
    return render_template("home.html", rows=leaderboard_rows)
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500


@home.route("/privacy-policy")
def policy():
  return render_template("privacy.html")


