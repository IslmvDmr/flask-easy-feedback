from flask import Blueprint, render_template, request, flash, g
from db import db, Pages, Seo

main = Blueprint('/', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html', seo_data=g.seo)


@main.route('/<string:page_name>', methods=['GET'])
def get_page(page_name):
    page = Pages.query.filter(Pages.url == page_name).first_or_404()

    return render_template("pages.html", page=page, seo_data=g.seo)


@main.before_request
def get_seo():
    seo = Seo.query.first()
    g.seo = {'title': seo.title, 'description': seo.title, 'keywords': seo.keywords}
