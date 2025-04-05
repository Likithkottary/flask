from app import app
from models.user_model import user_model

user_obj=user_model()

@app.route("/user")
def list_users():
    return user_obj.user_login_model()