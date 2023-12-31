from model import db, Person, app
from datetime import datetime

with app.app_context():
    man1 = Person("aaa", "070-5544-1111", 32, datetime.now(), datetime.now())
    man2 = Person("bbb", "070-6644-1111", 48, datetime.now(), datetime.now())
    man3 = Person("ccc", "070-7744-1111", 17, datetime.now(), datetime.now())

    # # 複数追加
    # db.session.add_all([man1, man2, man3])
    # # 実行
    # db.session.commit()

    # # 主キーでの取り出し
    # print(Person.query.get(3))

    # for x in Person.query.filter_by(name="taku").all():
    #     print(x.name)

    # データ削除
    # Person.query.filter_by(id=1).delete()
    # db.session.commit()

    # データ更新
    Person.query.filter_by(name="名無しさん").update(
        {"name": "John", "update_at": datetime.now()}
    )
    db.session.commit()
