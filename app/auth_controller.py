from flask import Blueprint, render_template, jsonify, send_file, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import DBSession, User
from sqlalchemy.orm import Session
import uuid

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home.homepage'))
  return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
  email = request.form.get('email')
  password = request.form.get('password')

  with DBSession() as session:
    user = session.query(User).filter(User.email == email).first()

  if not user or not check_password_hash(user.password, password): 
      flash('Please check your login details and try again.')
      return redirect(url_for('auth.login'))

  login_user(user, True)
  return redirect(url_for('home.homepage'))

@auth.route("/signup", methods=['GET'])
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('home.homepage'))
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
  email = request.form.get('email')
  username = request.form.get('username')
  password = request.form.get('password')
  confirm = request.form.get('confirm')

  passwords_dont_match = not (password == confirm)

  with DBSession() as session:
    email_exists = session.query(User).filter(User.email == email).first()
    username_exists = session.query(User).filter(User.username == username).first()
    
    if email_exists or username_exists or passwords_dont_match:
      if email_exists:
        flash('Email already in use.')
      if username_exists:
        flash('Username already in use.')
      if passwords_dont_match:
        flash('Passwords do not match.')
      return redirect(url_for('auth.signup'))

    new_user = User(
      email=email, 
      username=username, 
      password=generate_password_hash(password, method='sha256'), 
      zap_token=str(uuid.uuid4()))

    session.add(new_user)
    session.commit()

  return redirect(url_for('auth.login'))

@auth.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('auth.login'))
