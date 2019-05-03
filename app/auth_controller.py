from flask import Blueprint, render_template, jsonify, send_file, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import load_session, Users
from sqlalchemy.orm import Session

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET'])
def login():
  return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
  username = request.form.get('username')
  password = request.form.get('password')

  session = load_session()

  user = session.query(Users).filter(Users.username == username).first()

  session.close()

  if not user or not check_password_hash(user.password, password): 
      flash('Please check your login details and try again.')
      return redirect(url_for('auth.login'))


  login_user(user, True)
  return redirect(url_for('home.homepage'))

@auth.route("/signup", methods=['GET'])
def signup():
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
  username = request.form.get('username')
  password = request.form.get('password')

  session = load_session()

  if session.query(Users).filter(Users.username == username).first():
    flash('Email address already exists')
    return redirect(url_for('auth.signup'))

  new_user = Users(
    username=username, 
    password=generate_password_hash(password, method='sha256'), 
    zap_token="zap"+username)

  session.add(new_user)
  session.commit()
  session.close()

  return redirect(url_for('auth.login'))

@auth.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('auth.login'))
