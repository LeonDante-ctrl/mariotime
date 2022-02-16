import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField




class RegistrationForm(FlaskForm) :
  username
  email
  password
  confirm_password
  submit