# Flaskstudy

UdemyのFlask講座で学んだことまとめ  
Python+FlaskでのWebアプリケーション開発講座～0からFlaskをマスターしてSNSを作成する～ | Udemy https://www.udemy.com/course/flaskpythonweb/

# 各ディレクトリ概要
.  
├── 01_routing：ルーティングの流れが掴める  
├── 02_template：templateを用いたルーティング1  
├── 03_template_exam：templateを用いたルーティング2  
├── blueprint_sample：Blueprintを用いたアプリ分割    
├── form：フォームのPOST処理、画像アップロード  
├── login_sample：ログイン処理  
├── model_exam  
├── models  
├── models2  
├── models_foreignkey  
├── pdf：講座の参考資料  
├── requirements.txt：セクション5〜9までのパッケージ情報  
└── wtform：wtformsを使ったフォーム処理  

# 環境構築（virtualenv）

OS:Mac（Windowsだとやり方ちょっと変わる）  

①pythonをインストールした状態で、pythonのバージョンが選択されていることをチェックし、ターミナルで以下のコマンドを叩く
```
virtualenv 好きな環境名(仮にflaskenvとする)
```

②アクティベートする
```
. flaskenv/bin/activate
```

③アクティベート後、Flaskをインストール
```
pip install Flask
```

④requirements.txtからパッケージを一括インストール
```
pip freeze > requirements.txt
```

# 環境構築（miniconda）
①以下リンクより対応する.pkgをDLし、インストール（全てYESで進めてOK）  
https://docs.conda.io/projects/miniconda/en/latest/  

②ターミナルで環境確認  
```
conda env list
```

③仮想環境を構築
```
conda create --name pythonenv
```

④作った仮想環境をアクティベート
```
conda activate pythonenv
```

④環境を無効化する
```
conda deactivate
```

おまけ：miniconda導入するとターミナル開く度にデフォで(base)と記載されるので以下コマンドで設定変更する、表示されなくなる  
```
conda config --set auto_activate_base False
```

# ディレクトリの.pyファイル実行方法

①venv,virtualenv,もしくcondaをアクティベートする
```
. venv/bin/activate
```
②ターミナルで対象ディレクトリへ行き、対象の.pyファイルを選択し、以下のコマンドを叩く
```
flask --app XXX.py --debug run
```

またはVScodeで対象ファイル選択してメニュー上部「実行」->「デバッグ無しで実行」

# テーブル作成

テーブル作成用.pyファイルを実行
```
export FLASK_APP=models.py 
flask db init
flask db migrate -m "first commit"
flask db upgrade
```

