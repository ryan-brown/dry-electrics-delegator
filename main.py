from flask import Flask, request
import datetime

app = Flask(__name__)

user_data = {}

def rowHTML():
  sorted_data = sorted(user_data.items(), key=lambda kv: kv[1]["percentage"])

  html = ""
  for tup in sorted_data:
    name = tup[0]
    percentage = tup[1]["percentage"]
    time = tup[1]["time"]

    html += """<tr bgcolor="{}"><td>{}</td><td>{}</td><td>{}</td></tr>""".format(
      getRowColor(percentage),
      name,
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

@app.route("/")
def home():
  html = """
    <html>
      <head>
        <title>Dry Electrics Delegator</title>
        <script>setTimeout(() => window.location = window.location, 60 * 1000);<script>
      </head>
      <body bgcolor="#dddddd">
        <center>
          <h1>Dry Electrics Delegator</h1>
          <table border="1" style="width:25%">
            <tr>
              <th>User</th>
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
  user_data[data["username"]] = {
    "percentage": int(data["percentage"]),
    "time": datetime.datetime.now()
  }
  return "Success!"
