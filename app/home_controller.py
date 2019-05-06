from flask import render_template, Blueprint, redirect, url_for, request, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from qq import get_shitposts
from .models import User, DBSession

home = Blueprint('home', __name__)

@home.route("/")
def homepage():
  try:
    return render_template("home.html", shitposts=get_shitposts())
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500

@home.route("/settings", methods=['GET'])
@login_required
def show_settings():
  return render_template("settings.html")

@home.route("/settings", methods=['POST'])
@login_required
def save_settings():
  email = request.form.get('email')
  username = request.form.get('username')
  password = request.form.get('password')

  with DBSession() as session:
    email_exists = session.query(User).filter(User.id != current_user.id).filter(User.email == email).first()
    username_exists = session.query(User).filter(User.id != current_user.id).filter(User.username == username).first()

    if email_exists or username_exists:
      if email_exists:
        flash('Email already in use.')
      if username_exists:
        flash('Username already in use.')
      return redirect(url_for('home.show_settings'))

    user = session.query(User).filter(User.id == current_user.id).first()
    user.email = email
    user.username = username
    if password:
      user.password = generate_password_hash(password, method='sha256')
    session.commit()

  flash('Setting saved!')
  return redirect(url_for('home.show_settings'))

@home.route("/privacy-policy")
def policy():
  return render_template("privacy.html")
