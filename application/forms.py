"""Create form logic."""
# from flask_wtf import FlaskForm  ## deprecated
from wtforms import Form, StringField,PasswordField,SubmitField,validators


class SignupForm(Form):
    """User Signup Form."""

    name = StringField('Name*', [validators.DataRequired("Please enter  your name."),validators.Length(min=4, max=25)])
    email = StringField('Email Address*', [validators.DataRequired("Please enter  your email."),validators.Length(min=6, max=35)])
    password = PasswordField('New Password*', [validators.InputRequired(),validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password*',)
    website = StringField('Website')
    submit = SubmitField('Register')


class LoginForm(Form):
    """User Login Form."""

    email = StringField('Email Address', [validators.Length(min=6, max=35)])

    password = PasswordField('Password', [validators.InputRequired('Please enter a password')])
    submit = SubmitField('Log In')
