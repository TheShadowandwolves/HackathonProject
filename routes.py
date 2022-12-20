from flask import render_template, request, redirect, url_for, flash
from HackathonProject import app
import random


data = "home"
### app routes ###

@app.route('/')
@app.route('/home')
def home():

    print("dic")
    return render_template('home.html', dat = data)