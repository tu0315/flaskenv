from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h1>こんにちは。</h1>"


@app.route("/hello/<string:name1>/<string:name2>")
def show_name(name1, name2):
    return f"<h1>こんにちは{name1}さん,{name2}さん。</h1>"


@app.route("/add/<int:num1>/<int:num2>")
def add_num(num1, num2):
    add_num = num1 + num2
    return f"<h1>{add_num}</1>"


@app.route("/div/<float:num1>/<float:num2>")
def div_num(num1, num2):
    div_num = num1 / num2
    return f"<h1>{div_num}</1>"


if __name__ == "__main__":
    app.run(debug=True)
