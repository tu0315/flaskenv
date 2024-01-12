# セット
# 同じ値を持たないユニーク
# 順序が保持されない
# 集合処理を高速で行う事ができる
# リストは入れられない

set_a = {"a", "b", "c", "d", "a", 12}

# aは1つしか表示されない
print(set_a)

# eは含まれていないのでTrue
print("e" not in set_a)

# eは含まれていないのでFalse
print("e" in set_a)

# cは含まれてるのでTrue
print("c" not in set_a)

# 12は含まれているのでTrue
print(12 in set_a)

# setの長さ
print(len(set_a))

# add, remove, discard, pop, clear
set_a.add("e")
print(set_a)

# 削除
set_a.remove("e")
print(set_a)
# set_a.remove('E')
set_a.discard(12)
print(set_a)
set_a.discard(12)
print(set_a)
val = set_a.pop()
print(val)
print(set_a)
# 初期化
set_a.clear()
print(set_a)
