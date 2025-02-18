from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_manager, login_required, logout_user
from db import db, Feedback, Pages, Phones
from .forms import Pages_form

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@admin.route('/')
@login_required
def index():
    count_of_feedback = Feedback.query.count()
    count_of_calls = Phones.query.count()

    return render_template("main_admin.html", comments=count_of_feedback, calls=count_of_calls)


@admin.route('/pages')
@login_required
def pages():
    pages = Pages.query.order_by(Pages.date.desc())
    return render_template('admin_pages.html', pages=pages)


@admin.route('pages/add', methods=['GET', 'POST'])
@login_required
def add_pages():
    form = Pages_form()
    show_form = True
    if form.validate_on_submit():

        try:
            d = Pages(name=form.name.data, description=form.description.data, url=form.url.data)
            db.session.add(d)
            db.session.flush()
            db.session.commit()
            flash(f'Страница {form.name.data} добавлена!')
            show_form = False
            return redirect(url_for('admin.pages'))
        except:
            db.session.rollback()

    return render_template('add_page.html', form=form, show_form=show_form)


@admin.route('/pages/edit/<int:page_id>', methods=['POST', 'GET'])
@login_required
def edit_page(page_id):
    show_form = True
    page = Pages.query.get_or_404(page_id)
    form = Pages_form(name=page.name, description=page.description, url=page.url)
    if form.validate_on_submit():
        try:
            page.name = form.name.data
            page.url = form.url.data
            page.description = form.description.data
            db.session.commit()
            flash(f'Запись {form.name.data} обновлена')
            show_form = False
            return redirect(url_for('admin.pages'))
        except:
            db.session.rollback()

    return render_template('add_page.html', form=form, show_form=show_form)


@admin.route('/pages/delete/<int:page_id>', methods=['DELETE', 'GET'])
@login_required
def delete_page(page_id):
    try:
        page = Pages.query.get_or_404(page_id)
        db.session.delete(page)
        db.session.commit()
        flash('Запись удалена')
    except:
        db.session.rollback()
        flash('Ошибка удаления записи')
    return redirect(url_for('admin.pages'))


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))
