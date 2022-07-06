from flask import Blueprint, render_template, request, redirect, url_for, current_app
import datetime
from extentions import db
from models import User, Task
from flask_login import login_required, login_user

general = Blueprint("home", __name__, template_folder="templates", static_folder="static", static_url_path='/home')



@general.route('/')
@login_required
def index():
    get_user = User.query.filter_by(username='tylerjones4508').first()
    get_task = Task.query.filter_by(user_id=get_user.id).all()
    get_all_users = User.query.all()
    return render_template("home.html", user=get_user, task=get_task, all_users=get_all_users)
