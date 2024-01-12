# for

# for i in range(5):
#     print(i)

# 単に10回ループさせるだけ
# for _ in range(10):
#     print("A")
#     pass

# for i in range(2, 20, 3):
# print(i)

# # リスト
# sample = ["John", "Paul", "George", "Ringo"]

# for member in sample:
#     print(member)

# # タプルでも同じように
# sample = ("John", "Paul", "George", "Ringo")

# for member in sample:
#     print(member)

human = {"Name": "Taro", "Age": 20, "gender": "Man"}
for h in human:
    # keyとそれのvalueを表示
    print(h, human.get(h))
