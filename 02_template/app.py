from flask import Flask, render_template, redirect, url_for, abort

# 自分で作ったフィルター用.pyファイルをインポート
from custom_filters import reverse, birth_year

# インスタンス化
app = Flask(__name__)

# 自作.pyファイルの関数を使用
app.add_template_filter(reverse, "reverse_name")
app.add_template_filter(birth_year, "birth_year")


@app.route("/")
def index():
    return render_template("index.html")


# UserInfoクラス
class UserInfo:
    # 初期インスタンス
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    # あいさつ関数
    def greet(self):
        # 必ずリターンを用意する
        return f"{self.name}({self.age})です。趣味は{self.hobby}です。よろしくお願いいたします。"


@app.route("/home/<string:user_name>/<int:age>/<string:hobby>")
def home(user_name, age, hobby):
    # インスタンス化
    user_info = UserInfo(user_name, age, hobby)
    return render_template("home.html", user_info=user_info)
    # return render_template("home.html")


@app.route("/userlist")
def userlist():
    # リスト変数をセット
    users = ["taro", "jiro", "saburo", "siro", "takuro"]
    # boolean型の変数セット
    is_login = False
    # render_templateの引数にセットする
    return render_template("userlist.html", users=users, is_login=is_login)


# リダイレクト実践
@app.route("/user/<string:user_name>/<int:age>/<string:hobby>")
def user(user_name, age, hobby):
    if user_name in ["taro", "jiro", "takuro"]:
        # リダイレクトする
        return redirect(url_for("home", user_name=user_name, age=age, hobby=hobby))
    else:
        # 500エラーを発動させる
        abort(500, "そのユーザーはリダイレクトできません。")


# 404エラー時に発動するエラーハンドラー
@app.errorhandler(404)
def page_not_found(error):
    # テキトーなURLを入力すると再現可能
    return render_template("not_found.html"), 404


# 500エラー時に発動するエラーハンドラー
@app.errorhandler(500)
def system_error(error):
    print(error.description)
    # error.descriptionにはabortの第2引数がセットされている
    error_description = error.description
    return (
        render_template("system_error.html", error_description=error_description),
        500,
    )


if __name__ == "__main__":
    app.run(debug=True)
