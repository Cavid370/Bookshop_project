from venv import create
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField, EmailField
from wtforms.validators import DataRequired,Length, Email

class CommentForm(FlaskForm):
    fullname = StringField(label='fullname',name="fullname", validators=[DataRequired(),Length(min=3,max=40)], render_kw={'placeholder':'Enter your Fullname'})
    language = SelectField(label='languages',name='language',choices=[("aze","Azərbaycan"),("eng","İngilis"),("ru","Rus")])
    message= TextAreaField(label="message",name="message",validators=[], render_kw={'placeholder':'Your message:'})
    # create_at = StringField()


class RegisterForm(FlaskForm):
    first_name = StringField(label='first_name',name="first_name", validators=[DataRequired(),Length(min=3,max=30)], render_kw={'placeholder':'First Name'})
    last_name = StringField(label='last_name',name="last_name", validators=[DataRequired(),Length(min=3,max=30)], render_kw={'placeholder':'Last Name'})
    email = EmailField(label='email',name="email", validators=[DataRequired(),Length(min=3,max=30)], render_kw={'placeholder':'exp@gmail.com'})
    username = StringField(label='username',name="username", validators=[DataRequired(),Length(min=3,max=30)], render_kw={'placeholder':'Username'})
    password = StringField(label='password',name="password", validators=[DataRequired(),Length(min=8,max=255)], render_kw={'placeholder':'Password'})


class LoginForm(FlaskForm):
    username = StringField(label='username',name="username", validators=[DataRequired(),Length(min=3,max=30)], render_kw={'placeholder':'Username'})
    password = StringField(label='password',name="password", validators=[DataRequired(),Length(min=8,max=255)], render_kw={'placeholder':'Password'})
