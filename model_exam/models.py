from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

# dbインスタンス作成
db = SQLAlchemy(app)
# マイグレートする
Migrate(app, db)


# Memberクラス
class Member(db.Model):
    # テーブル名
    __tablename__ = "members"

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    comment = db.Column(db.Text)

    # インスタンス作成時に実行
    def __init__(self, name, age, comment):
        self.name = name
        self.age = age
        self.comment = comment


# 実行する
# with app.app_context():
#     db.create_all()
