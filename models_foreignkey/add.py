from model import db, Employee, Project, Company, app

# 外部キーを用いたテーブル定義及びデータ追加
with app.app_context():
    # 従業員情報
    jack = Employee("jack")
    dia = Employee("dia")

    # 追加
    db.session.add_all([jack, dia])
    db.session.commit()

    # 会社情報
    company1 = Company("Microsoft", jack.id)
    company2 = Company("Google", dia.id)

    # 追加
    db.session.add_all([company1, company2])
    db.session.commit()

    # プロジェクト情報
    project1 = Project("Word", jack.id)
    project2 = Project("Excel", dia.id)
    project3 = Project("Pixel", jack.id)
    project4 = Project("Drive", dia.id)

    # 追加
    db.session.add_all([project1, project2, project3, project4])
    db.session.commit()
