from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "hello liki"

@app.route("/login")
def login():
    return "hello login page"

from controller import *





