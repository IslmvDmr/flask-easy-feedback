from flask import Flask, render_template, flash
from feedback import fb
from admin import admin
from flask_sqlalchemy import SQLAlchemy
from forms import Phone

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SECRET_KEY'] = 'sqlite:///app.db'
    from db import db, migrate, Phones
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(fb, url_prefix='/feedback')
    app.register_blueprint(admin, url_prefix='/admin')

    @app.route('/', methods=['GET', 'POST'])
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

        return render_template('main.html', form=form, register_phone=register_phone)

    return app


if __name__ == "__main__":
    create_app().run("0.0.0.0", debug=True)
