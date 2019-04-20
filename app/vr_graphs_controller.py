from flask import render_template, Blueprint
import maya
import cgi
import database

vr_graphs = Blueprint('vr_graphs', __name__)

@vr_graphs.route("/<username>")
def vr_homepage(username):
  try:
      return render_template("vr_graphs.html", username=username)
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500
