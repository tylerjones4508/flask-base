from flask import Blueprint, render_template, request, redirect, url_for, current_app
import datetime
from extentions import db, bcrypt
from models import User
from flask_login import current_user, login_user, logout_user

auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static", static_url_path="/auth")

@auth.route("/login", methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        get_user = User.query.filter_by(username=username).first()

        if get_user and bcrypt.check_password_hash(get_user.password, password):
            login_user(get_user)
            return redirect(url_for('home.index'))
            
    return render_template('login.html')


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/register", methods=['GET', 'POST'])
def resgister():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        firstname = request.form.get('fname')
        lastname = request.form.get('lname')
        email = request.form.get('email')
        hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
        create_user = User(
            username=username, first_name=firstname, last_name=lastname,
            email=email, password=hash_password
        )
        db.session.add(create_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')