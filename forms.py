from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class Phone(FlaskForm):
    name = StringField("Имя ", validators=[DataRequired(), Length(min=1, max=30)])
    phone = StringField("Телефон ", validators=[DataRequired(), Length(min=11, max=11)])
    submit = SubmitField("Отправить")


class Feedback_form(FlaskForm):
    name = StringField("Ваше имя ", validators=[DataRequired(), Length(min=1, max=30)])
    email = StringField("Электронная почта", validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField("Напишите ваш отзыв о товаре или услуге",
                                validators=[DataRequired(), Length(min=1, max=500), ])
    submit = SubmitField("Отправить")


class Claim(FlaskForm):
    name = StringField("Ваше имя ", validators=[DataRequired(), Length(min=1, max=30)])
    email = StringField("Электронная почта", validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField("Напишите чем вы недовольны", validators=[DataRequired(), Length(min=1, max=500), ])
    submit = SubmitField("Отправить")
