from flask import render_template, request, redirect, url_for, flash
from HackathonProject import app
import random



### app routes ###

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form')
def paper():
    return render_template('form.html')