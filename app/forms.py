from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from authy.api import AuthyApiClient
from config import Config

from app.models import User

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type your password', validators=[DataRequired(), EqualTo('password')])
    phoneNumber = StringField('Phone Number',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address")

class VerificationForm(FlaskForm):
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])
    code = StringField('Verification Field', validators=[DataRequired()])
    submit = SubmitField('Verify')