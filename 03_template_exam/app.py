from flask import Flask, render_template, redirect, url_for

# フラスクのインスタンス化
app = Flask(__name__)


# ユーザーclass化
class UserInfo:
    # 初期インスタンス
    def __init__(self, number, name, age, gender, major, picture_path):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.picture_path = picture_path


# 使用するメンバーリスト
member_list = [
    UserInfo(0, "太郎", 21, "男", "法学部", "image/taro.jpg"),
    UserInfo(1, "次郎", 20, "男", "理学部", "image/jiro.jpg"),
    UserInfo(2, "良子", 22, "女", "文学部", "image/ryoko.jpg"),
    UserInfo(3, "花子", 21, "女", "工学部", "image/hanako.jpg"),
]


# メインページ
@app.route("/")
def main():
    return render_template("main.html")


# メンバー一覧ページ
@app.route("/memberlist")
def load_member_list():
    return render_template("member_list.html", member_list=member_list)


# メンバー毎の詳細ページ
@app.route("/member/<int:member_number>")
def load_member_detail(member_number):
    for member in member_list:
        # 一致したメンバーがいたら詳細ページへ
        if member.number == member_number:
            return render_template("member_detail.html", member=member)


# 利用規約
@app.route("/terms")
def terms_of_service():
    return render_template("terms.html")


# 404時はメインにリダイレクト
@app.errorhandler(404)
def redirect_main_page(error):
    return redirect(url_for("main"))


# デバッグありで実行
if __name__ == "__main__":
    app.run(debug=True)
