from flask import render_template, request, redirect, url_for, flash, jsonify
from HackathonProject import app
import random
import requests
import json

def get_location():
    send_url = "http://api.ipstack.com/check?access_key=YOUR_ACCESS_KEY"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
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