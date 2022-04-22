from flask.helpers import flash
from flask import render_template, redirect, url_for, request
from app_center.process.dashboard import app_dashboard_init, model_dashboard, controller_dashboard
from werkzeug.security import generate_password_hash, check_password_hash
from app_center import db
from flask_login import login_user, login_required, current_user, logout_user


@app_dashboard_init.route('/dashboard')
def dashboard():
  return render_template('home/dashboard.html')