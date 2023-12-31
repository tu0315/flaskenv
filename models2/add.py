from model import db, Person, app
from datetime import datetime

with app.app_context():
    man1 = Person(None, "070-2244-1111", 32, datetime.now(), datetime.now())

    # 1つ追加
    db.session.add(man1)
    # 実行
    db.session.commit()
