import datetime


# templateで使えるfilterをカスタムして追加
# 文字を逆順にするfilter
def reverse(name):
    return name[::-1]


# 生まれ年を表示するfilter
def birth_year(age):
    # 現在の年
    current_year = datetime.datetime.now().year
    # 生まれた年をざっくり算出して返す
    birth_year = current_year - age
    return birth_year
