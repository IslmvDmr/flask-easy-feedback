from flask import Blueprint

fb = Blueprint('call', __name__, template_folder='templates', static_folder='static')

@fb.route('/')
def fb_main():
    return 'call'