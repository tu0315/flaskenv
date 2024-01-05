# Flaskstudy

UdemyのFlask講座で学んだことまとめ  
Python+FlaskでのWebアプリケーション開発講座～0からFlaskをマスターしてSNSを作成する～ | Udemy https://www.udemy.com/course/flaskpythonweb/

# 環境構築

OS:Mac（Windowsだとやり方ちょっと変わるかも！）  
virtualenvを使用する

①pythonをインストールした状態で、pythonのバージョンが選択されていることをチェックし、ターミナルで以下のコマンドを叩く
```zsh
virtualenv 好きな環境名(仮にflaskenvとする)
```

②アクティベートする
```zsh
. flaskenv/bin/activate                    
flask --app app --debug run
```

③アクティベート後、Flaskをインストール
```zsh
pip install Flask
```

④requirements.txtからパッケージを一括インストール
```zsh
pip freeze > requirements.txt
```

# ディレクトリの.pyファイル実行方法

①venv,virtualenv,もしくcondaをアクティベートする
```zsh
. venv/bin/activate
```
②ターミナルで対象ディレクトリへ行き、対象の.pyファイルを選択し、以下のコマンドを叩く
```flask
flask --app XXX.py --debug run
```

またはVScodeで対象ファイル選択してメニュー上部「実行」->「デバッグ無しで実行」

# テーブル作成

テーブル作成用.pyファイルを実行
```python
export FLASK_APP=models.py 
flask db init
flask db migrate -m "first commit"
flask db upgrade
```