# for i in range(10):
#     if i == 3 or i == 5:
#         # 3と5の時飛ばす
#         continue
#     print(i)
# else:
#     print("ループ処理終了")

# やってることは一緒
num = 0
while num < 10:
    if num == 5:
        # +1して飛ばす
        num += 1
        continue
    if num == 9:
        # 終
        break
    print(num)
    num += 1
else:
    print("whileループ終了")
