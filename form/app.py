from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# インポートされない(pip installはできており、pip listにも既存のパッケージライブラリ同様に表示される。pip show pykakasiも効く。installしている実行環境も既存の場所と変わらず。)
# import pykakasi
import os


# flaskのインスタンス化
app = Flask(__name__)


# Pykakasiで変換（importできてないので使えてないが。質問する）
# class Kakashi:
#     kakashi = pykakasi.kakasi()
#     kakashi.setMode("H", "a")
#     kakashi.setMode("K", "a")
#     kakashi.setMode("J", "a")
#     conv = kakashi.getConverter()

#     @classmethod
#     def japanese_to_ascii(cls, japanese):
#         return cls.conv.do(japanese)


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
    # *GET, POSTに対応
    user_info = UserInfo(
        request.form.get("last_name"),
        request.form.get("first_name"),
        request.form.get("job"),
        request.form.get("gender"),
        request.form.get("message"),
    )
    # *更に良いやり方がFlaskにはある!

    return render_template("home.html", user_info=user_info)


# 画像ファイルアップロード
@app.route("/upload", methods=["GET", "POST"])
def upload():
    # GET時の処理
    if request.method == "GET":
        return render_template("upload.html")
    # POST時の処理
    elif request.method == "POST":
        # POSTデータからファイル名取得
        file = request.files["file"]
        # ファイルを日本語から英語に変換
        # ascii_filename = Kakashi.japanese_to_ascii(file.filename)
        # ファイル名を安全な形式に変換
        save_filename = secure_filename(file.filename)
        # ファイルを保存する
        # os.path.dirname(__file__)でapp.pyを指し示す
        file.save(
            os.path.join(os.path.dirname(__file__), "static/image", save_filename)
        )
        return redirect(url_for("uploaded_file", filename=save_filename))


# ファイルアップロード完了
@app.route("/uploaded_file/<string:filename>")
def uploaded_file(filename):
    return render_template("uploaded_file.html", filename=filename)


# デバッグありで実行
if __name__ == "__main__":
    app.run(debug=True)
