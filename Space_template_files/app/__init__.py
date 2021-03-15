from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from flask import jsonify, make_response
from wtforms import StringField, SubmitField


class UserForm(FlaskForm):
    fname = StringField("first Name")
    lname = StringField("last Name")
    email = StringField("Email")
    submit = StringField("submit")

app=Flask(__name__)
app.config['SECRET_KEY']='Longasdjkfhkj'

from app import views

