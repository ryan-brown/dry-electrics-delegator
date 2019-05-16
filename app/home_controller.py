from flask import render_template, Blueprint, redirect, url_for, request, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from qq import get_shitposts
from .models import User, DBSession
from .user_policy import *
import uuid
import os

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
  confirm = request.form.get('confirm')
  new_zap = request.form.get('new_zap')

  passwords_dont_match = not (password == confirm)

  username_errors = validate_username(username)
  email_errors = validate_email(email)
  password_errors = password and validate_password(password)

  if username_errors or email_errors or password_errors or passwords_dont_match:
    for error in username_errors:
      flash(error)
    for error in email_errors:
      flash(error)
    for error in password_errors:
      flash(error)
    if passwords_dont_match:
      flash("Passwords do not match.")
    return redirect(url_for('home.show_settings'))

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
    old_username = user.username
    user.email = email
    user.username = username
    if password:
      user.password = generate_password_hash(password, method='sha256')
    if new_zap:
      user.zap_token = str(uuid.uuid4())
    session.commit()

    image_template = 'app/static/profile_pictures/{}.png'
    exists = os.path.isfile(image_template.format(old_username))
    if exists and old_username != username:
      os.rename(image_template.format(old_username), image_template.format(username))

  flash('Setting saved!')
  return redirect(url_for('home.show_settings'))

@home.route("/privacy-policy")
def policy():
  return render_template("privacy.html")

@home.route("/uploader", methods=['POST'])
@login_required
def upload_image():
  try:
    f = request.files['file']
    f.save(os.path.join('app/static/profile_pictures', current_user.username+".png"))
    flash('Profile picture updated!')
    return redirect(url_for('home.show_settings'))
  except Exception as e:
    print(e)
    flash('Error uploading image.')
    return redirect(url_for('home.show_settings'))
