import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, CheckConstraint

# model.pyを配置しているファイルのパスを格納
base_dir = os.path.dirname(__file__)

# flaskのインスタンス化
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# dbインスタンス作成
db = SQLAlchemy(app)


# Personクラス
class Person(db.Model):
    # テーブル名
    __tablename__ = "persons"
    # チェック制約
    __table_args__ = (CheckConstraint("update_at >= create_at"),)  # チェック制約

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(20), index=True, server_default="名無しさん"
    )  # Indexを設定したため、名前での検索が高速
    phone_number = db.Column(
        db.String(13), nullable=False, unique=True
    )  # NOT NULL, UNIQUE
    age = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.DateTime)
    update_at = db.Column(db.DateTime)

    # インスタンス作成時に実行
    def __init__(self, name, phone_number, age, create_at, update_at):
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.create_at = create_at
        self.update_at = update_at

    # 中身を返す
    def __str__(self):
        return f"id = {self.id}, name = {self.name}, phone_number = {self.phone_number}, age = {self.age}, create_at = {self.create_at},update_at = {self.update_at}"


# クラスの外からインデックスを追加
db.Index("my_index", func.lower(Person.name))

# 実行する
with app.app_context():
    db.create_all()
