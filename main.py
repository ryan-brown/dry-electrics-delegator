from flask import Flask, request
import maya
import cgi
import datetime
import os

app = Flask(__name__)

user_data = {}

def rowHTML():
  sorted_data = sorted(user_data.items(), key=lambda kv: kv[1]["percentage"])

  html = ""
  for tup in sorted_data:
    name = tup[0]
    percentage = tup[1]["percentage"]
    time = maya.parse(tup[1]["time"], timezone='US/Eastern').slang_time()
    charging = "🔌 ⚡" if tup[1]["charging"] else  "🔋 "

    html += """<tr bgcolor="{}"><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>""".format(
      getRowColor(percentage),
      name,
      charging,
      percentage,
      time)

  return html

def toHex(num):
  res = hex(num)[2:]

  if num < 16:
    res = "0"+res

  return res

def getRowColor(percentage):
  if percentage <= 50:
    red = 255
    green = round(255 * percentage * 2 / 100)
  else:
    red = round(255 * (1 - (percentage - 50) * 2 / 100))
    green = 255

  return "#{}{}00".format(toHex(red), toHex(green))

@app.route("/update", methods=['GET', 'POST'])
def update():
  os.system("git pull origin master")
  return "Done"

@app.route("/")
def home():
  html = """
    <html>
      <head>
        <title>Dry Electrics Delegator</title>
        <script>setTimeout(() => window.location = window.location, 60 * 1000);</script>
      </head>
      <body bgcolor="#dddddd">
        <center>
          <h1>Dry Electrics Delegator</h1>
          <table border="1" style="width:25%">
            <tr>
              <th>User</th>
              <th>Status</th>
              <th>Percentage</th>
              <th>Updated At</th>
            </tr>
            {}
          </table>
          TEST HOT RELOAD
        </center>
      </body>
    </html>""".format(rowHTML())

  return html

@app.route("/percentage", methods=['POST'])
def percentage():
  data = request.get_json()
  username = cgi.escape(data["username"])
  try:
    percentage = int(data["percentage"])
    if percentage < 0 or percentage > 100 or len(username) > 16:
      return "fuck you"

    charging = bool(data["charging"])
  except:
    return "still fuck you"

  user_data[username] = {
    "percentage": percentage,
    "charging": charging,
    "time": maya.now().datetime(to_timezone='US/Eastern')
  }
  return "Success!"
