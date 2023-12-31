from model import db, Person, app

with app.app_context():
    # dbを実行
    db.create_all()

    # データ用意
    man1 = Person("taku", 27)
    man2 = Person("jiro", 15)
    man3 = Person("sabu", 45)
    print(man1, man2, man3)

    # dbに追加する
    # 複数追加
    db.session.add_all([man1, man2])
    # 1つ追加
    db.session.add(man3)
    # 実行
    db.session.commit()
    print(man1, man2, man3)

    # 拡張機能SQLiteで中身を確認可能
