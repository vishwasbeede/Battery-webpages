from app import app,render_template,request,redirect,url_for
from test import *

@app.route("/")
def root_fun():

    return render_template('public/templates/index.html')


@app.route("/new.html")
def return_fun():
    return render_template("new.html",names="Ganesh")

@app.route("/new.html")
def return_fun1_1_1():
    return render_template("new.html",names="Ganesh")

@app.route("/new.html")
def return_fun2_1():
    return render_template("new.html",names="Ganesh")

@app.route("/animals")
def return_fun2():
    return render_template("aniamls.html",z=packed)