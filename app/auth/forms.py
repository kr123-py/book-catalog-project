from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.templates.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(3, 15, message="between 3 to 15 character")])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    Password = PasswordField('Password',
                             validators=[DataRequired(), Length(5), EqualTo('confirm', message='Password must '
                                                                                               'match')])
    confirm = PasswordField('confirm', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay logged-in')
    submit = SubmitField('LogIn')
