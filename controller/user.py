# Python imports
import datetime
import jwt
# Flask imports
from flask import render_template, flash, redirect, url_for, jsonify, make_response, request
from flask_login import current_user, login_user, logout_user

# Project imports
from controller import app
from controller import db
from model.user import User
from form.register import *

__Author__ = "Amir Mohammad"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect('/scrape')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/api_1/get_token', methods=['POST'])
def authorization():
    auth = request.authorization
    if auth and auth.username == 'amir' and auth.password == '9128020911':
        token = jwt.encode(
            {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify(jsonify={'token': token.decode('UTF-8')}), 200

    return make_response({'message': 'Could not verify token'}, 401,
                         {'WWW-Authenticate': 'Basic real="Login Required"'})
