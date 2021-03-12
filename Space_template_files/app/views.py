from app import app,render_template,request,redirect,url_for
from test import *

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

@app.route("/")
def root_fun():
    return render_template('public/templates/index.html')

# @app.route("/blog/")
@app.route("/blog/")
def return_fun():
    return render_template("new.html",names="Blog")

@app.route("/new.html")
def return_fun1_1_1():
    return render_template("new.html",names="Ganesh")

@app.route("/new.html")
def return_fun2_1():
    return render_template("new.html",names="Ganesh")

@app.route("/animals")
def return_fun2():
    return render_template("aniamls.html",z=packed)

# @app.route("/animals1")
# def GreetUserForm():
#     username = StringField(label=("Enter your name"))
#     submit = SubmitField(label=("submit"))
#     return ""

@app.route("/Products/")
def products_page():
    return render_template("aniamls.html",z=packed)

@app.route("/Blog/")
def Blog_page():
    return render_template("aniamls.html",z=packed)

@app.route("/Contact/")
def Contact_page():
    return render_template("aniamls.html",z=packed)

@app.route("/Careers/")
def Careers_page():
    return render_template("aniamls.html",z=packed)