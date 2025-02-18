from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class Pages_form(FlaskForm):
    name = StringField("Название страницы ", validators=[DataRequired(), Length(min=1, max=80)])
    url = StringField("Ссылка на страницу", validators=[DataRequired(), Length(min=1, max=80)])
    description = TextAreaField("Текст ", validators=[DataRequired(), Length(min=4, max=1000)])
    submit = SubmitField("Отправить")