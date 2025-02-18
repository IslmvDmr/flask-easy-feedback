from flask import Blueprint, render_template, request, flash
from forms import Feedback_form, Phone
from db import db, Feedback, Phones

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

    return render_template('main_fb.html', form=form, register_phone=register_phone)
@fb.route('/comment', methods=['GET', 'POST'])
def fb_main():
    form = Feedback_form()  # Создаем экземпляр формы внутри функции
    if request.method == 'POST' and form.validate_on_submit():
        try:
            add_feedback = Feedback(name=form.name.data, email=form.email.data, message = form.description.data)
            db.session.add(add_feedback)
            db.session.flush()
            db.session.commit()
            flash(f'{form.name.data}, спасибо за отзыв! ')
            form = Feedback_form(formdata=None)
        except:
            db.session.rollback()
    return render_template('feedback.html', form=form)

@fb.route('/claim', methods=['GET', 'POST'])
def claim():
    return render_template('claim.html')