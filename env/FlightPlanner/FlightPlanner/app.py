from flask import Flask, render_template, request
from django.shortcuts import render
from forms import airports
from distance import distance

app = Flask(__name__)

@app.route('/')
def index():
    return('index.html')


@app.route('/', methods=['GET', 'POST'])
def startAirport():
    form = airports()
    if form.is_submitted():
        result = request.form
    return render_template('index.html', result = result)
