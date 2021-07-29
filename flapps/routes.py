from flask import render_template, url_for, request, redirect, flash
from flapps import app, db
from flask_login import login_user, logout_user, login_required, current_user




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login form"

    if request.method == 'POST':
        Name=request.form['name']
        Age=request.form['age']
        cur= db.connection.cursor()
        cur.execute("INSERT INTO user(Name,username) VALUES (%s, %s)", (Name,Age))
        db.connection.commit()
        cur.close()
        return f"Done!!"