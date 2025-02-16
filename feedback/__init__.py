from flask import Blueprint, render_template

fb = Blueprint('feedback', __name__)

@fb.route('/')
def fb_main():
    return render_template('feedback.html')