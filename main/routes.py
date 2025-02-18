from flask import Blueprint, render_template, request, flash
from db import db, Pages

main = Blueprint('/', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')


@main.route('/<string:page_name>', methods=['GET'])
def get_page(page_name):
    page = Pages.query.filter(Pages.url == page_name).first_or_404()

    return render_template("pages.html", page = page)
