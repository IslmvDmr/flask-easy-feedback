from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from forms import Feedback_form, Phone
from db import db, Feedback, Phones,Seo

fb = Blueprint('feedback', __name__)


@fb.route('/', methods=['GET', 'POST'])
def index():
    form = Phone()
    if form.validate_on_submit():
        register_phone = True
        try:
            add_phone = Phones(name=form.name.data, number=form.phone.data)
            db.session.add(add_phone)
            db.session.flush()
            db.session.commit()
            flash(f'{form.name.data}, благодарим за обращение. В скором времени с вами свяжутся по телефону.')
        except:
            db.session.rollback()

    else:
        register_phone = False

    return render_template('main_fb.html', form=form, register_phone=register_phone, seo_data=g.seo)


@fb.route('/comment', methods=['GET', 'POST'])
def fb_main():
    show_form = True
    form = Feedback_form()  # Создаем экземпляр формы внутри функции
    if request.method == 'POST' and form.validate_on_submit():
        try:
            add_feedback = Feedback(name=form.name.data, email=form.email.data, message=form.description.data,
                                    type="Отзыв")
            db.session.add(add_feedback)
            db.session.flush()
            db.session.commit()
            flash(f'{form.name.data}, спасибо за отзыв! ')
            form = Feedback_form(formdata=None)
            show_form = False
            return redirect(url_for('feedback.index'))
        except:
            db.session.rollback()
    return render_template('feedback.html', form=form, show_form=show_form, seo_data=g.seo)


@fb.route('/claim', methods=['GET', 'POST'])
def claim():
    return render_template('claim.html')


@fb.before_request
def get_seo():
    seo = Seo.query.first()
    g.seo = {'title': seo.title, 'description': seo.title, 'keywords': seo.keywords}
