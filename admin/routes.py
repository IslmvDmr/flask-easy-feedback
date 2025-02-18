from flask import Blueprint, render_template,redirect, url_for
from flask_login import LoginManager, login_user, login_manager, login_required, logout_user

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

@admin.route('/')
@login_required
def index():
    return render_template('admin.html')

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))