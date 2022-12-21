from flask import render_template, request, redirect, url_for, flash, jsonify
from HackathonProject import app
from HackathonProject import parse, WhisperLive
import random
import requests
import json



def get_json():
    data = parse.Parse()
    return data

def go_record():
    WhisperLive.main()

def stop_record():
    with open("stop.txt","w+") as f:
        f.write("True")

### app routes ###

@app.route('/')
@app.route('/home')
def home():
    data = {}
    return render_template('home.html', data = data)

@app.route('/button-click', methods=['POST'])
def handle_button_click():
    data = request.get_json()
    value = data['value']
    print(value)
    if (value == '1'):
        go_record()
    elif (value == '0'):
        stop_record()
    return 'ok'


@app.route('/data')
def get_data():
    data = get_json()
    return jsonify(data)

@app.route('/tableIndex')
def tableIndex():
    return render_template('tableIndex.html')