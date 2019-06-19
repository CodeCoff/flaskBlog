#this is a flask extension
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

from flaskblog.models import User
'''
this module is for forms that will be used in our site. e.g. registration form, user form etc.
It utilizes the wtforms library that does most of the heavy lifting for us.
'''

#this is a registration form
class RegistrationForm(FlaskForm):
    #Anything inside a ' ' is a label
    #username for the user. Validators help us validate the 'username' value
    #e.g. here we are validating that the username is not empty with 'Datarequired',
    # 'Length' helps us validate the username string length (2-20)
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=5, max=20)])
        
    #email for the user. 'Email' validator is used to make sure it's the email address
    email = StringField('Email', validators=[DataRequired(), Email()])
        
    #password for the user. 'PasswordField' helps us hide the typed password
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])

    #confirm_password for the user. 'EqualTo' helps us compare with the 'password'
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    #'SubmitField' helps us send the information to the database
    submit = SubmitField('Sign Up')

    #validate if the username already exist. We are passing username here but we could check with other User fields
    def validate_username(self, username):
        #check if the user already exist in the database
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one!')
    
    #validate if the email already exist. We are passing username here but we could check with other User fields
    def validate_email(self, email):
        #check if the user already exist in the database
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one!')

#this is a login form that the user will used to log in to our system
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    #Anything inside a ' ' is a label
    #username for the user. Validators help us validate the 'username' value
    #e.g. here we are validating that the username is not empty with 'Datarequired',
    # 'Length' helps us validate the username string length (2-20)
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=5, max=20)])
        
    #email for the user. 'Email' validator is used to make sure it's the email address
    email = StringField('Email', validators=[DataRequired(), Email()])

    picture = FileField('Update Profile Pictue', validators=[FileAllowed(['jpg', 'png'])])
        
    #'SubmitField' helps us send the information to the database
    submit = SubmitField('Update')

    #validate if the username already exist. We are passing username here but we could check with other User fields
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one!')
    
    #validate if the email already exist. We are passing username here but we could check with other User fields
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('That email is taken. Please choose a different one!')
