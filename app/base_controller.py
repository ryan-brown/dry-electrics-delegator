from flask import Blueprint, send_from_directory
import database
import os

base = Blueprint('base', __name__)

@base.route('/static/<filename>')
def static(filename):
  return send_from_directory(os.path.join(base.root_path, 'static'), filename)

@base.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(base.root_path, 'static'), 'favicon.png',mimetype='image/png')

@base.route("/update", methods=['GET', 'POST'])
def update():
  try:
    os.system("git pull origin master")
    return "Done", 200
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500
