from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, IntegerField
from wtforms.form import Form


# flaskのインスタンス化
app = Flask(__name__)

# シークレットキーの設定、os.urandom(16)で出力された乱数を設定する
app.config["SECRET_KEY"] = b"_\xa3\xa0y\x15\x1b\xbd\x9cU\xed\x9c\x9e\xf3\xb2\x0f\x05"


# UserFormクラス
class UserForm(Form):
    name = StringField("名前")
    age = IntegerField("年齢")
    submit = SubmitField("Submit")


# indexページ
@app.route("/", methods=["GET", "POST"])
def index():
    name = age = ""
    # UserFormに値を入力
    form = UserForm(request.form)
    # POSTで入力されたら
    if request.method == "POST":
        # バリデーションに引っかからなかったら
        if form.validate():
            # 値を入力
            name = form.name.data
            age = form.age.data
            # form初期化
            form = UserForm()
        else:
            # エラーを返す
            print("入力内容に問題があります。")
    # 引数に値をセットしてレンディングする(GETでアクセスしたときは上記の処理通らないよ)
    return render_template("index.html", form=form, name=name, age=age)


# デバッグありで実行
if __name__ == "__main__":
    app.run(debug=True)
