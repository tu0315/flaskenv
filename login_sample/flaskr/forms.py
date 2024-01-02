from wtforms.form import Form
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User


# ログインフォーム
class LoginForm(Form):
    email = StringField("メール: ", validators=[DataRequired(), Email()])
    password = PasswordField("パスワード: ", validators=[DataRequired()])
    submit = SubmitField("ログイン")


# 登録フォーム
class RegisterForm(Form):
    email = StringField("メール: ", validators=[DataRequired(), Email()])
    username = StringField("名前: ", validators=[DataRequired()])
    password = PasswordField(
        "パスワード: ",
        validators=[
            DataRequired(),
            EqualTo("password_confirm", message="パスワードが一致しません"),
        ],
    )
    password_confirm = PasswordField("パスワード確認: ", validators=[DataRequired()])
    submit = SubmitField("登録")

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError("メールアドレスは既に登録済みです。")
