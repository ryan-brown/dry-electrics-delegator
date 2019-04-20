from flask import Blueprint, render_template, send_file
import database
import qq 
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
    all_users = qq.get_all_users()
    user_data = { name: qq.get_user_data(str(name)) for name in all_users }
    user_data_items = user_data.items()
    sorted_user_data = [item[1] for item in sorted(user_data.items(), key=lambda kv: kv[0][1])]
    formatted_user_data = [(get_row_color(d['percentage']), d['username'], d['percentage'], "🔌 " if d['charging'] else  "🔋 ", maya.parse(d['updated_at'], timezone='US/Eastern')) for d in sorted_user_data]
    return [(d[0], d[1], d[2], d[3], d[4].epoch) for d in formatted_user_data if (maya.now() - d[4]).total_seconds() < 60*10]

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
  return json.dumps(get_leaderboard())

@api.route("/stats/<username>")
def user_stats(username):
  user_data = [[d[2], d[3], str(d[4])] for d in database.get_user_data(username)]
  return json.dumps(user_data)
