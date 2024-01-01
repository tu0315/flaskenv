from wtforms import Form
from wtforms.fields import (
    HiddenField,
    StringField,
    IntegerField,
    SubmitField,
)


# 新しいメンバーを作るためのフォーム
class CreateMemberForm(Form):
    name = StringField("名前は: ")
    age = IntegerField("年齢は: ")
    comment = StringField("コメントは: ")
    submit = SubmitField("作成")


# メンバーを更新するためのフォーム
class UpdateMemberForm(Form):
    id = HiddenField()
    name = StringField("名前は: ")
    age = IntegerField("年齢は: ")
    comment = StringField("コメントは: ")
    submit = SubmitField("作成")


# メンバーを削除するためのフォーム
class DeleteMemberForm(Form):
    id = HiddenField()
    submit = SubmitField("削除")
