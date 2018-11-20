from flask import render_template, Blueprint, send_file
import database
import maya
import os

home = Blueprint('home', __name__)

def get_leaderboard():
  user_data = database.select_all()
  sorted_user_data = sorted(user_data, key=lambda tup: tup[2])

  formatted_user_data = [(get_row_color(d[2]), d[1], d[2], "🔌 " if d[3] else  "🔋 ", maya.parse(d[4], timezone='US/Eastern')) for d in sorted_user_data]
  return [(d[0], d[1], d[2], d[3], d[4].slang_time()) for d in formatted_user_data if (maya.now() - d[4]).total_seconds() < 60*10]


def to_hex(num):
  res = hex(num)[2:]

  if num < 16:
    res = "0"+res

  return res

def get_row_color(percentage):
  if percentage <= 50:
    red = 255
    green = round(255 * percentage * 2 / 100)
  else:
    red = round(255 * (1 - (percentage - 50) * 2 / 100))
    green = 255

  return "#{}{}00".format(to_hex(red), to_hex(green))

@home.route("/")
def homepage():
  try:
    leaderboard_rows = get_leaderboard()
    return render_template("home.html", rows=leaderboard_rows)
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500

@home.route("/db")
def get_db():
  return send_file("../database.db", as_attachment=True)

  
@home.route("/db_size")
def db_size():
  return str(os.path.getsize("database.db"))

@home.route("/privacy-policy")
def policy():
  return render_template("privacy.html")


