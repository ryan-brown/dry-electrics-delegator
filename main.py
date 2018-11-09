from flask import Flask, request, send_from_directory
import maya
import cgi
import datetime
import os
import database

app = Flask(__name__)

def rowHTML():
  user_data = database.select_all()
  sorted_user_data = sorted(user_data, key=lambda tup: tup[2])

  html = ""
  for tup in sorted_user_data:
    name = tup[1]
    percentage = tup[2]
    charging = "🔌 " if tup[3] else  "🔋 "
    updated_at = maya.parse(tup[4], timezone='US/Eastern')

    seconds_since_update = (maya.now() - updated_at).total_seconds()
    if seconds_since_update > 60*10:
      continue

    html += """<tr bgcolor="{}"><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>""".format(
      get_row_color(percentage),
      name,
      charging,
      percentage,
      updated_at.slang_time())

  return html

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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/update", methods=['GET', 'POST'])
def update():
  os.system("git pull origin master")
  return "Done", 200

@app.route("/")
def home():
  html = """
    <html>
      <head>
        <title>Dry Electrics Delegator</title>
        <script>setTimeout(() => window.location = window.location, 60 * 1000);</script>
        <link rel="shortcut icon" href="/favicon.ico">
        <style type="text/css">
          table {{
            width: 50%;
            border: 1px solid black;
            border-collapse: collapse;
          }}

          td {{
            padding: 1rem;
            font-family: 'helvetica neue', helvetica, arial, sans-serif;
            text-align: center;
            border: none;
            border-bottom: 1px solid black;
          }}

          th {{
            font-size: larger;
            padding: .5rem;
            border: none;
            border-bottom: 2px solid black;
          }}
        </style>
      </head>
      <body bgcolor="#dddddd">
        <center>
          <h1>Dry Electrics Delegator</h1>
          <table border="1">
            <tr>
              <th>User</th>
              <th>Charging</th>
              <th>Percentage</th>
              <th>Updated At</th>
            </tr>
            {}
          </table>
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
      return "Reported percentage out of bounds", 400

    charging = bool(data["charging"])
    updated_at = maya.now().datetime(to_timezone='US/Eastern')

    database.insert_update(username, percentage, charging, updated_at)

    return "Success", 200
  except:
    return "An unexpected error has occurred, please try again later", 500

