from flask import Flask  # Flaskをインポート

# アプリケーションを立ち上げるインスタンス、テンプレート読み込みのときなどに使用する
# Flaskクラスのインスタンスを作って、appという変数に代入している
# __name__ というのは、自動的に定義される変数で、現在のファイルのモジュール名が入る。
# ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
app = Flask(__name__)


@app.route("/")  # /にアクセス（デコレータ関数）
def index():  # index関数
    return "<h1>Indexページ</h1>"  # 値を返す


@app.route("/hello")  # /helloにアクセス
def hello():  # hello関数
    return "<h1>hello,world!!</h1>"  # 値を返す


@app.route("/post/<int:post_id>/<post_name>")  # post/<整数値:post_id>/<post_name>にアクセス
def show_post(post_id, post_name):  # show_post関数。引数にpost_id, post_name
    return f"{post_id}: {post_name}"  # 引数を返す


# 辞書型の変数posts()
posts = {
    1: "POST1",
    2: "POST2",
}


@app.route("/get_post/<int:post_id>")  # get_post/<整数値:post_id>にアクセス
def show_get_post(post_id):  # show_get_post関数。引数にpost_id
    post = posts.get(post_id)  # 上記の辞書型変数からgetで取得、存在しなければNoneを返す
    return f"{post}"  # postを返す


# user/<文字型:user_name>/<数値型:user_number>にアクセス
@app.route("/user/<string:user_name>/<int:user_number>")
def show_user(user_name, user_number):
    user_name_number = f"{user_name}: {user_number}"
    return f"<h1>{user_name_number}</h1>"


if __name__ == "__main__":
    # 本番環境では環境変数を設定するのが一般的（export FLASK_APP=XX.py）
    app.run(debug=True)  # アプリケーションを立ち上げるためのメソッド。debugありで実行
    # アクセスログにGETしたURLが表示されるよ
