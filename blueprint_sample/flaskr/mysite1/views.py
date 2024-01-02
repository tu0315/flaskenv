from flask import Blueprint, render_template

mysite1_bp = Blueprint("mysite1", __name__, url_prefix="/site1")


@mysite1_bp.route("/hello")
def hello():
    return render_template("mysite1/hello.html")
