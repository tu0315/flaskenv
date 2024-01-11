# 文字列型

fruit = "apple"  # ""
print(fruit)
print(type(fruit))

print(fruit * 10)

new_fruit = fruit + " banana"
print(new_fruit)

# """
fruits = """apple
banana
grape
"""
print(fruits)

fruit = "banana"
print(fruit[0])  # b

# encode, decode(bytes[]型の関数) => bytes[]
byte_fruit = fruit.encode("utf-8")

print(byte_fruit)
print(type(byte_fruit))
str_fruit = byte_fruit.decode("shift-jis")
print(str_fruit)
print(type(str_fruit))

# count関数

msg = "ABCDEABC"

print(msg.count("A"))

# # startswith endswith

print(msg.startswith("ABCD"))
print(msg.endswith("ABC"))

# #　strip, rstrip, lstrip

msg = "  ACB  "
print(msg.strip())
msg = "ABCDEABC"
print(msg.strip("ACB"))
print(msg.rstrip("ACB"))
print(msg.lstrip("ACB"))

# # upper, lower, swapcase, replace, capitalize

msg = "abcABC"
msg_u = msg.upper()  # 大文字
msg_l = msg.lower()  # 小文字
msg_s = msg.swapcase()  # 大文字小文字入れ替え

print(msg_u)
print(msg_l)
print(msg_s)

msg = "ABCDEABC"
msg_r = msg.replace("ABC", "FFF", 1)  # 文字変換
print(msg_r)

msg = "hELLO world"
print(msg.capitalize())  # 最初だけ大文字

# 文字列の一部取り出し、format関数、文字列から数値への変換、islower, isupper
msg = "hello"
print(msg.isupper())  # 大文字？
print(msg.islower())  # 小文字？

msg = "hello, my name is taro"

print(msg[0:4])  # 4番目までを取り出す
print(msg[6:])  # 6番目以降を取り出す
print(msg[1:6])  # 1から6番目を取り出す
print(msg[1:10:2])  # 1つ飛ばして取得

name = "Hanako"
msg = f"my name is {name}"  # 3.6
msg = f"my name is {name=}"  # 3.8

print(msg)

msg = "12.21"
int_msg = float(msg)
print(int_msg)
print(type(int_msg))
# find, index, rfind, rindex

msg = "ABCDEABC"
print(msg.rfind("ABDC"))
