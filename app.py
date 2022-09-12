from flask import Flask
app = Flask(__name__)
import random

@app.route('/')
def hello_world():
    return str(random.random())
