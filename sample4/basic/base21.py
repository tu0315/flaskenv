# セイウチ演算子
# =の前に:をつけた演算子

# nへの代入と比較を同時に行っている
if (n := 3) > 5:
    print("5より大きい: {}".format(n))
else:
    print("5より小さい: {}".format(n))

n = 0
# 簡潔に書くことができる
while (n := n + 1) <= 10:
    print(n)
