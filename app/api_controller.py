from flask import Blueprint, render_template, send_file, jsonify, request
import database
import qq 
import json
import maya

api = Blueprint('api', __name__)

COLOR_RED = {
    "red": 196,
    "green": 2,
    "blue": 51
  }
COLOR_YELLOW = {
    "red": 255,
    "green": 211,
    "blue": 0
  }
COLOR_GREEN = {
    "red": 0,
    "green": 159,
    "blue": 107
  }

def rbg_to_hex(r,g,b):
  r = hex(int(r))[2:]
  g = hex(int(g))[2:]
  b = hex(int(b))[2:]

  if (len(r) == 1):
    r = "0" + r
  if (len(g) == 1):
    g = "0" + g
  if (len(b) == 1):
    b = "0" + b

  return "#" + r + g + b

def get_row_color(percentage):
  if (percentage < 0.5):
    color1 = COLOR_RED
    color2 = COLOR_YELLOW
    percentage *= 2
  else:
    color1 = COLOR_YELLOW
    color2 = COLOR_GREEN
    percentage = 2 * (percentage - 0.5)

  red = color1["red"] + percentage * (color2["red"] - color1["red"])
  green = color1["green"] + percentage * (color2["green"] - color1["green"])
  blue = color1["blue"] + percentage * (color2["blue"] - color1["blue"])
  
  return rbg_to_hex(red, green, blue)

def get_leaderboard():
    all_users = qq.get_all_users()
    user_data = { name: qq.get_user_data(str(name)) for name in all_users }
    user_data_items = user_data.items()
    sorted_user_data = [item[1] for item in sorted(user_data_items, key=lambda kv: kv[1]['percentage'])]
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

@api.route("v2/driest")
def driest2():
    all_users = get_leaderboard()
    human_text = "no one"
    if len(all_users) >= 1:
        lowest = all_users[0]
        human_text = "%s at %d percent" % (lowest[1], lowest[2])
    return human_text

@api.route("/database")
def db():
  return send_file("../database.db", as_attachment=True)

@api.route("/stats")
def stats():
  return json.dumps(get_leaderboard())

@api.route("/shitpost", methods=['POST'])
def shitpost():
    shit = request.get_json()
    qq.add_shit(shit)
    return 'nice one'
