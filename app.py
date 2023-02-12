import sqlite3
from flask import Flask, render_template, request, g, redirect

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')
    
@app.get('/form')
def home():
    return render_template('form.html')


@app.post('/new_user')
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    return redirect('/')
