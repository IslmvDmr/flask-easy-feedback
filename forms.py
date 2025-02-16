from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class Phone(FlaskForm):
    name = StringField("Имя ", validators=[DataRequired(), Length(min=1, max=30)])
    phone = StringField("Телефон ", validators=[DataRequired(), Length(min=4, max=10)])
    submit = SubmitField("Отправить")