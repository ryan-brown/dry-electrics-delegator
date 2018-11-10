from flask import Flask, request, send_from_directory
import maya
import cgi
import datetime
import os
import database

from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
