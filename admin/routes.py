from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_manager, login_required, logout_user, current_user
from db import db, Feedback, Pages, Phones, User, Seo
from .forms import Pages_form, AdminPassword, Seo_form

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@admin.route('/')
@login_required
def index():
    count_of_feedback = Feedback.query.count()
    count_of_calls = Phones.query.count()
    phones = Phones.query.all()
    messages = Feedback.query.order_by(Feedback.id.desc()).limit(5)
    phones = Phones.query.order_by(Phones.id.desc()).limit(5)

    return render_template("main_admin.html", comments=count_of_feedback, calls=count_of_calls, messages=messages,
                           phones=phones)


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


@admin.route('/feedback')
@login_required
def feedback():
    feedback = Feedback.query.order_by(Feedback.date.desc())
    return render_template('feedback_list.html', feedback=feedback)


@admin.route('/feedback/<int:page_id>', methods=['GET'])
@login_required
def feedback_show(page_id):
    page = Feedback.query.first_or_404(page_id)
    return render_template('show_feedback.html', page=page)


@admin.route('/feedback/delete/<int:page_id>', methods=['GET'])
@login_required
def delete_feedback(page_id):
    try:
        page = Feedback.query.get_or_404(page_id)
        db.session.delete(page)
        db.session.commit()
        flash('Запись удалена')
    except:
        db.session.rollback()
        flash('Ошибка удаления записи')
    return redirect(url_for('admin.feedback'))

@admin.route('/calls')
@login_required
def calls():
    calls = Phones.query.order_by(Phones.date.desc())
    return render_template('calls_list.html', calls=calls)

@admin.route('/calls/delete/<int:page_id>', methods=['GET'])
@login_required
def delete_call(page_id):
    try:
        call = Phones.query.get_or_404(page_id)
        db.session.delete(call)
        db.session.commit()
        flash('Запись удалена')
    except:
        db.session.rollback()
        flash('Ошибка удаления записи')
    return redirect(url_for('admin.calls'))

@admin.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = AdminPassword()
    if form.validate_on_submit():
        try:
            _user = User.query.first_or_404(current_user.id)
            _user.email = form.name.data
            _user.set_password(form.password.data)
            db.session.commit()
            flash(f'Пароль изменен')
        except:
            flash('Что то пошло не так')
    return render_template("change_password.html", form=form)


@admin.route('/configs', methods=['GET', 'POST'])
@login_required
def seo_configs():
    seo = Seo.query.get_or_404(1)
    form = Seo_form(title=seo.title, description=seo.description, keywords=seo.keywords)
    if form.validate_on_submit():
        seo.title = form.title.data
        seo.description = form.description.data
        seo.keywords = form.keywords.data
        db.session.commit()
        flash(f'Запись обновлена')

    return render_template("configs.html", form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))
