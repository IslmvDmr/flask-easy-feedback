from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from db import User
from db import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.index'))
        else:
            flash('Ошибка входа')
            return render_template('login.html')
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    return render_template('login.html')




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
