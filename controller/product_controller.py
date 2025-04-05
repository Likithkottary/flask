from app import app
from models.product_model import product_model

obj_product_model = product_model()

@app.route("/products")
def list_product():
    return obj_product_model.product_list_model()

@app.route("/products/add")
def add_product_controller():
    return obj_product_model.product_add_model()

@app.route("/products/remove")
def remove_product_controller():
    return obj_product_model.product_remove_model()