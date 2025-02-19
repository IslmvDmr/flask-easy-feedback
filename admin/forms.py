from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class Pages_form(FlaskForm):
    name = StringField("Название страницы ", validators=[DataRequired(), Length(min=1, max=80)])
    url = StringField("Ссылка на страницу", validators=[DataRequired(), Length(min=1, max=80)])
    description = TextAreaField("Текст ", validators=[DataRequired(), Length(min=4, max=1000)])
    submit = SubmitField("Отправить")

class Seo_form(FlaskForm):
    title = StringField("Название сайта ", validators=[DataRequired(), Length(min=1, max=300)])
    description = TextAreaField("Описание сайта", validators=[DataRequired(), Length(min=1, max=300)])
    keywords = StringField("Ключевые слова(через запятую) ", validators=[DataRequired(), Length(min=4, max=100)])
    submit = SubmitField("Отправить")

class AdminPassword(FlaskForm):
    name = StringField("Логин", validators=[DataRequired(), Length(min=1, max=80)])
    password = PasswordField("Пароль", validators=[DataRequired(), Length(min=1, max=80)])
    password2 = PasswordField("Повторите пароль", validators=[DataRequired(),
                                                               EqualTo('password', message="Пароли не совпадают"), Length(min=4, max=1000)])
    submit = SubmitField("Отправить")