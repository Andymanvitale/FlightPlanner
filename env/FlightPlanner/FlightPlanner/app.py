from flask import Flask, render_template, request
from django.shortcuts import render
from forms import airports
from getDistance import findDistance

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