import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Flask‐loginアプリケーションを立ち上げる
login_manager = LoginManager()
# ログインの関数
login_manager.login_view = "app.login"
# ログインへのリダイレクト時のメッセージ
login_manager.login_message = "ログインしてください"

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    pass
