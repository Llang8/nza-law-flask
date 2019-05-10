from app import app,db
from flask import render_template, flash,redirect,url_for
from app.forms import LoginForm,RegistrationForm,VerificationForm
from app.models import User
from app.verification import createVerification, verifyVerification
#flask_login imports
from flask_login import current_user,login_user,logout_user,login_required

import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/who')
def who():
    return render_template('who.html')

@app.route('/what')
def what():
    return render_template('what.html')

@app.route('/register',methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    # Validate form on submit
    if form.validate_on_submit():
        user = User(email=form.email.data,password_hash=form.password.data)
        user.set_password(form.password.data)
        createVerification(form.phoneNumber.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have successfully registered')
        return redirect(url_for('verify'))

    return render_template('register.html',form=form)

@app.route('/login',methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        
        login_user(user,remember=form.remember_me.data)
        flash('Login Requested for user {}, remember_me = {}'.format(form.email.data,form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html',title="Sign In",form=form)

@app.route('/verify', methods=["GET","POST"])
def verify():
    form = VerificationForm()
    if form.validate_on_submit():
        # if verifyVerification(form.phoneNumber.data,form.code.data):
        return redirect(url_for('index'))

    return render_template('verify.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))