from flask import render_template, Blueprint
import database
import os
from qq import get_shitposts

from .api_controller import get_leaderboard

home = Blueprint('home', __name__)

@home.route("/")
def homepage():
  try:
    return render_template("home.html", shitposts=get_shitposts())
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500


@home.route("/privacy-policy")
def policy():
  return render_template("privacy.html")
