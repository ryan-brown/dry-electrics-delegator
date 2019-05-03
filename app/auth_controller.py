from flask import Blueprint, render_template, jsonify, send_file, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import DBSession, User
from sqlalchemy.orm import Session
import uuid

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET'])
def login():
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
  return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
  email = request.form.get('email')
  username = request.form.get('username')
  password = request.form.get('password')

  with DBSession() as session:
    user = session.query(User).filter(User.email == email or User.username == username).first()

    if user:
      flash('Email or Username already exists.')
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
