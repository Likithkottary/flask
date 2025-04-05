from flask import Flask, jsonify
app=Flask(__name__)

@app.route("/")
def index():
    data={
        "id":"001",
        "name":"liki"
    }
    return jsonify(data)

@app.route("/login")
def login():
    return "hello login page"

from controller import *





