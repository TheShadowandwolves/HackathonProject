from flask import render_template, request, redirect, url_for, flash, jsonify
from HackathonProject import app
from HackathonProject import parse
#from HackathonProject import WhisperLive
import random
import requests
import json



def get_json():
    parse.Parse()
    # with open("data.json","r") as f:
    #     data = json.load(f)
    datas = {'lastName': 'John', 'firstName': 'Done'}

    return render_template('home.html', data = datas)

def go_record():
   # WhisperLive.main()
    print("done recording")
    pass

def stop_record():
    with open("stop.txt","w+") as f:
        f.write("True")

### app routes ###

@app.route('/')
@app.route('/home')
def home():
    
    data = {'lastName': 'Levin', 'firstName': 'Peretz'}
  
    return render_template('home.html', data = data)

@app.route('/button-click', methods=['POST'])
def handle_button_click():
    data = request.get_json()
    value = data['value']
    print(value)
    if (int(value) == 1):
        go_record()
    elif (value == 0):
        stop_record()
    return 'ok'


@app.route('/fetch-data', methods=['POST'])
def get_data():
    data= {}
   
    valu =request.get_json()
    print(valu)
    val = valu['value']
    print(val)
    if (int(val) == 1):
        data = {'lastName': 'Doe', 'firstName': 'John'}
        print(data)
    return redirect(url_for('home', data = data))
    # return 'ok'

@app.route('/tableIndex')
def tableIndex():
    return render_template('tableIndex.html')