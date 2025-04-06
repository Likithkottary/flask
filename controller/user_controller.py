from app import app
from models.user_model import user_model
from flask import jsonify
from flask import request

user_obj=user_model()

@app.route("/user")
def list_users():
    data = user_obj.user_login_model()
    return jsonify(data)

@app.route("/user/add",methods=["POST"])
def add_users():
    return user_obj.user_add_model(request.form)

@app.route("/user/update",methods=["PUT"])
def update_users():
    return user_obj.user_update_model(request.form)

@app.route("/user/delete/<id>",methods=["DELETE"])
def delete_users(id):
    return user_obj.user_delete_model(id)
     