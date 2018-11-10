from flask import Flask, request, send_from_directory
import maya
import cgi
import datetime
import os
import database

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app