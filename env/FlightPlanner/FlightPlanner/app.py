from flask import Flask, render_template, request
from django.shortcuts import render
from forms import airports
from getDistance import findDistance
import requests
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return('index.html')

#Dont think I need this
@app.route('/', methods=['GET', 'POST'])
def startAirport():
    form = airports()
    if form.is_submitted():
        result = request.form
    return render_template('index.html', result = result)

@app.route('/')
def getDis():
    calc = findDistance()
    return render_template('index.html', result = calc)

req = requests.get("https://api.checkwx.com/metar/KJFK?x-api-key=5df00ce5a84046e4ad91f3cca5")

@app.route('/')
def metar():
    try:
        req.raise_for_status()
        resp = json.loads(req.text)
        return render_template('index.html', result = resp)

    except requests.exceptions.HTTPError as e:
        print(e)