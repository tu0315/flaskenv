# 辞書の関数
car = {"brand": "Toyota", "model": "Prius", "year": 2015}
print(car)

tmp_dict = {"country": "Japan", "prefecture": "Aichi", "model": "カローラ"}
car.update(tmp_dict)
print(car)
car["city"] = "Toyota-shi"
car["year"] = 2024
print(car)

value = car.popitem()
print(car)
print(value)

# キーの値取り出し
value = car.pop("model")
print(car)
print(value)

car.clear()
print(car)

# del car
# print(car)
