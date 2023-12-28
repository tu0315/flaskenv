from flask import Flask, render_template, request

# flaskのインスタンス化
app = Flask(__name__)


# ユーザーclass
class UserInfo:
    # 初期インスタンス
    def __init__(self, last_name, first_name, job, gender, message):
        self.last_name = last_name
        self.first_name = first_name
        self.job = job
        self.gender = gender
        self.message = message


# サインアップページ
@app.route("/signup")
def sign_up():
    return render_template("signup.html")


# ホーム画面
@app.route("/home", methods=["GET", "POST"])
def home():
    # ターミナル上にフォームから送ったデータを表示する
    print(request.full_path)
    print(request.method)
    print(request.args)

    # UserInfoクラスのインスタンス作成
    # *以下だとGET時しか取得できない
    # user_info = UserInfo(
    #     request.args.get("last_name"),
    #     request.args.get("first_name"),
    #     request.args.get("job"),
    #     request.args.get("gender"),
    #     request.args.get("message"),
    # )
    # GET, POSTに対応
    user_info = UserInfo(
        request.form.get("last_name"),
        request.form.get("first_name"),
        request.form.get("job"),
        request.form.get("gender"),
        request.form.get("message"),
    )
    # 更に良いやり方がFlaskにはある！

    return render_template("home.html", user_info=user_info)


# デバッグありで実行
if __name__ == "__main__":
    app.run(debug=True)
