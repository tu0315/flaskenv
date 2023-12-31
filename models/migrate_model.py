import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# model.pyを配置しているファイルのパスを格納
base_dir = os.path.dirname(__file__)

# flaskのインスタンス化
app = Flask(__name__)
# データを格納する場所
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "migrate_data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# dbインスタンス作成
db = SQLAlchemy(app)
Migrate(app, db)
# ターミナルで~/Documents/Python/flaskstudy/modelsまで移動して、以下を実行
# export FLASK_APP=migrate_model.py
# flask db init
# Migrationを設定するファイルを生成する
# flask db migrate -m "add persons"
# DBを反映
# flask db upgrade


# Personクラス
class Person(db.Model):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    gender = db.Column(db.Text)
    age = db.Column(db.Integer)

    # インスタンス作成時に実行
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 中身を返す
    def __str__(self):
        return f"id = {self.id}, name = {self.name}, age = {self.age},"
