from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from flaskr.forms import LoginForm, RegisterForm
from flaskr.models import User

bp = Blueprint("app", __name__, url_prefix="")


# ホーム
@bp.route("/")
def home():
    return render_template("home.html")


# ウェルカムページ
# ログインしていないと実行されない
# ログインしてなければlogin関数に飛ばされる
@bp.route("/welcome")
@login_required
def welcome():
    return render_template("welcome.html")


# ログアウト実行
@bp.route("/logout")
@login_required
def logout():
    # ログアウトする
    logout_user()
    return redirect(url_for("app.home"))


# ログインページ
@bp.route("/login", methods=["GET", "POST"])
@login_required
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.select_by_email(form.email.data)
        # emailから取得したUserのパスワードとクライアントが入力したパスワードが一致しているか
        if user and user.validate_password(form.password.data):
            # ログインする
            login_user(user)
            # 次のURLを取得する
            next = request.args.get("next")
            if not next:
                next = url_for("app.welcome")
            return redirect(next)
    return render_template("login.html", form=form)


# 登録ページ
@bp.route("/register", methods=["GET", "POST"])
@login_required
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
        )
        user.add_user()
        return redirect(url_for("app.login"))
    return render_template("register.html", form=form)


# userページ
@bp.route("/user")
@login_required
def user():
    return render_template("user.html")
