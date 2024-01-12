# タプル
# タプルは値を追加することはできない
# 配列よりもアクセスが早い
# ハッシュ化した辞書キーとして利用できる
# 値を変更したくないような値に使うと、変更されないことを保障できる

fruit = ("apple", "banana", "lemon")

print(fruit)
print(type(fruit))
print(fruit[0])

# 値を変更できないのでエラーになる
# fruit[1] = "grape"

# 値を追加する
fruit = fruit + ("grape",)
print(fruit)

# リストの値をタプルに追加する
list_fruit = ["apple", "banana"]
fruit = tuple(list_fruit)
print(fruit)
print(fruit.count("apple"))
print(fruit.index("apple"))

pos = (135, 35)

countries = {pos: "Japan"}

print(countries.get((135, 35)))
