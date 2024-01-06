from flaskr import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin


# セッションに保存されたログインユーザを返すためにtemplateから呼ばれる
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# UserMixInはFlask-loginライブラリを利用するユーザが持つべきオブジェクトを定義する
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))

    # コンストラクタ
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    # パスワード確認用関数、正しいかどうか返す
    def validate_password(self, password):
        return check_password_hash(self.password, password)

    # ユーザー追加
    def add_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def select_by_email(cls, email):
        # emailでUserを絞り込む
        return cls.query.filter_by(email=email).first()
