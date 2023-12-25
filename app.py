from flask import Flask  # Flaskをインポート

# アプリケーションを立ち上げるインスタンス、テンプレート読み込みのときなどに使用する
app = Flask(__name__)  # ルーティングで必要な変数。Flaskの中心となる。nameで場所を伝えてる？？？よくわかんね


@app.route("/")  # /にアクセス（デコレータ関数）
def index():  # index関数
    return "<h1>usuki</h1>"  # 値を返す


@app.route("/hello")  # /helloにアクセス
def hello():  # hello関数
    return "<h1>hello,world!!</h1>"  # 値を返す


# 辞書型の変数posts
posts = {
    1: "POST1",
    2: "POST2",
}


# 変数でルーティング先を動的に変更する、型定義も可能
@app.route("/post/<int:post_id>/<post_name>")  # post/<整数値:post_id>/<post_name>にアクセス
def show_post(post_id, post_name):  # show_post変数。引数にpost_id, post_name
    # post = posts.get(post_id) # getで取得
    # post = posts[post_id]  # 鉤括弧で取得
    # return f"{post}"  # postsから取得
    return f"{post_id}: {post_name}"  # 引数を返す


@app.route("/user/<string:user_name>/<int:user_number>")
def show_user(user_name, user_number):
    user_name_number = f"{user_name}: {user_number}"
    return f"<h1>{user_name_number}</h1>"


if __name__ == "__main__":  # nameには__main__が入っている
    # 本番環境では環境変数を設定するのが一般的（export FLASK_APP=XX.py）
    app.run(debug=True)  # アプリケーションを立ち上げるためのメソッド。debugありで実行
    # アクセスログにGETしたURLが表示されるよ
