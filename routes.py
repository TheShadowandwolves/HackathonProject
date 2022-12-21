from flask import render_template, request, redirect, url_for, flash, jsonify
from HackathonProject import app
import random
import requests
import json
def get_location():
    city = "New York"
    return city


### app routes ###

@app.route('/')
@app.route('/home')
def home():
    data ={ "typeName": "test", 
            "date": "date",
            "time": "time",
            "location": "location",
            "currentlocation": get_location()

            }
    print("dic")
    return render_template('home.html', data = data)

@app.route('/data')
def get_data():
    data = {'key': 'new value'}
    return jsonify(data)

@app.route('/tableIndex')
def tableIndex():
    return render_template('tableIndex.html')