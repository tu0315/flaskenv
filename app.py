from flask import Flask

app = Flask(__name__)  # アプリケーション立ち上げのインスタンス(__name__は、テンプレート読み込みの時などに内部で使用)


@app.route("/")  # デコレータ関数(後続の関数に処理を追加)
def index():  # index関数
    """ルートURLへのアクセス"""
    return "<h1>usuki</h1>"


@app.route("/hello")
def hello():
    """/helloに対応"""
    return "<h1>hello,world</h1>"


posts = {
    1: "POST1",
    2: "POST2",
}


@app.route("/post/<int:post_id>/<post_name>")
def show_post(post_id, post_name):
    """特定の投稿を表示 post_id:整数値"""
    post = posts.get(post_id)
    return f"{post_id}: {post_name}"


@app.route("/user/<string:user_name>/<int:user_number>")
def show_user(user_name, user_number):
    user_name_number = f"{user_name}: {user_number}"
    return f"<h1>{user_name_number}</h1>"


if __name__ == "__main__":
    app.run(debug=True)  # debugありで実行
