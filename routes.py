from flask import render_template, request, redirect, url_for, flash
from HackathonProject import app
import random



### app routes ###

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')