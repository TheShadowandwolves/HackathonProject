from flask import render_template, request, redirect, url_for, flash, jsonify
from HackathonProject import app
import random
import requests
import json
def get_location():
    city = "New York"
    return city

def get_json():
    pass

### app routes ###

@app.route('/')
@app.route('/home')
def home():
    data = get_json()
    print("dic")
    return render_template('home.html', data = data)

@app.route('/data')
def get_data():
    data = {'key': 'new value'}
    return jsonify(data)

@app.route('/tableIndex')
def tableIndex():
    return render_template('tableIndex.html')