from flask import Blueprint, render_template, request, flash


main = Blueprint('/', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

