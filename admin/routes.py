from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_manager, login_required, logout_user
from db import db, Feedback, Pages
from .forms import Pages_form

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@admin.route('/')
@login_required
def index():
    count_of_feedback = Feedback.query.count()

    return str(count_of_feedback)


@admin.route('/pages')
@login_required
def pages():
    pages = Pages.query.order_by(Pages.date.desc())
    return render_template('pages.html', pages = pages)


@admin.route('/add_page', methods=['GET', 'POST'])
@login_required
def add_pages():
    form = Pages_form()
    show_form = True
    if form.validate_on_submit():

        try:
            d = Pages(name=form.name.data, description = form.description.data, url=form.url.data)
            db.session.add(d)
            db.session.flush()
            db.session.commit()
            flash(f'Страница {form.name.data} добавлена!')
            show_form = False
        except:
            db.session.rollback()

    return render_template('add_page.html', form=form, show_form = show_form)

@admin.route('/edit_page/<int:page_id>', methods=['PUT', 'GET'])
@login_required
def edit_page(page_id):
    page = Pages.query.get_or_404(page_id)
    pass

@admin.route('/pages/delete/<int:page_id>', methods=['DELETE', 'GET'])
@login_required
def delete_page(page_id):
    page = Pages.query.get_or_404(page_id)
    db.session.delete(page)
    db.session.commit()
    return 'deleted'


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))


