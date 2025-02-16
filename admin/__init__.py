from flask import Blueprint, render_template
from flask_login import LoginManager, login_user



admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
login_manager = LoginManager()




class UserLogin:
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user['id'])


@admin.route('/')
def fb_main():
    return render_template('login.html')

@admin.route('/control')
def control_panel():
    return render_template('admin.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    login_manager.login_user(user, remember=False, duration=None, force=False, fresh=True)

