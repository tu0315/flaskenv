import os
from flask import Flask

# model.pyを配置しているファイルのパスを格納
base_dir = os.path.abspath(os.path.dirname(__file__))

# flaskのインスタンス化
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
