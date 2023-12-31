import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# model.pyを配置しているファイルのパスを格納
base_dir = os.path.abspath(os.path.dirname(__file__))

# flaskのインスタンス化
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    base_dir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True  # SQLを吐き出してくれるオプション

# dbインスタンス作成
db = SQLAlchemy(app)


# Employeeクラス
class Employee(db.Model):
    # テーブル名
    __tablename__ = "employees"

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # 紐ついた情報を取得する
    # one to many
    projects = db.relationship("Project", backref="employees")
    # one to one
    company = db.relationship("Company", backref="employees", uselist=False)

    # インスタンス作成時に実行
    def __init__(self, name):
        self.name = name

    # 中身を返す
    def __str__(self):
        if self.company:
            return f"Employee name = {self.name} company is {self.company}"
        else:
            return f"Employee name = {self.name} has no company"

    # プロジェクト一覧を返す
    def show_projects(self):
        for project in self.projects:
            print(project.name)


# Projectクラス
class Project(db.Model):
    # テーブル名
    __tablename__ = "projects"

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"))

    # インスタンス作成時に実行
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


# Companyクラス
class Company(db.Model):
    # テーブル名
    __tablename__ = "companys"

    # カラム情報
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"))

    # インスタンス作成時に実行
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


# 実行する
with app.app_context():
    db.create_all()
