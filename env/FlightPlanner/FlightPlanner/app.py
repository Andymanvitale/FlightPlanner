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


req = requests.get("https://api.checkwx.com/metar/KJFK?x-api-key=5df00ce5a84046e4ad91f3cca5")