# セットの関数

s = {"a", "b", "c", "d"}
t = {"c", "d", "e", "f"}

u = s | t  # 和集合UNION、どちらかにある要素
u = s.union(t)  # 和集合

print(u)

u = s & t  # 積集合、共通要素
u = s.intersection(t)

print(u)

u = s - t  # 差集合、片方にあり片方にない
u = s.difference(t)
print(u)

u = s ^ t
u = s.symmetric_difference(t)
print(u)

s |= t  # => s = s | t => sがsとtの和集合=>sにtの要素が入る
print(s)

# issubset, issuperset, isdisjoint
s = {"apple", "banana"}
t = {"apple", "banana", "lemon"}
u = {"cherry"}

# 比較
print(s.issubset(t))
print(s.issuperset(t))
print(t.isdisjoint(s))
print(t.isdisjoint(u))
