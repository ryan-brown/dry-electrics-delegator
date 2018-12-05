from flask import Blueprint, render_template, send_file
import database
import json
import maya
from flask import jsonify

api = Blueprint('api', __name__)


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

def get_leaderboard():
  user_data = database.select_all()
  sorted_user_data = sorted(user_data, key=lambda tup: tup[2])
  formatted_user_data = [(get_row_color(d[2]), d[1], d[2], "🔌 " if d[3] else  "🔋 ", maya.parse(d[4], timezone='US/Eastern')) for d in sorted_user_data]
  return [(d[0], d[1], d[2], d[3], d[4]) for d in formatted_user_data if (maya.now() - d[4]).total_seconds() < 60*10]

@api.route("/driest")
def driest():
    all_users = get_leaderboard()
    human_text = "no one"
    if len(all_users) >= 1:
        lowest = all_users[0]
        human_text = "%s at %d percent" % (lowest[1], lowest[2])

    return jsonify({
      "fulfillmentText": human_text,
      "payload": {
        "google": {
          "expectUserResponse": False,
          "richResponse": {
          "items": [{
              "simpleResponse":{
                "textToSpeech": human_text
              }
            }
          ]
        }
      }
    }})

@api.route("/database")
def db():
  return send_file("../database.db", as_attachment=True)

@api.route("/stats")
def stats():
  return str(get_leaderboard())
