# !/usr/bin/python3

varTypeDic = {0: "value0", 1: "value1", 2: "value2", "3": "value3", "4": 4}
print(varTypeDic)
print(varTypeDic[0], end=" ")
print(varTypeDic["3"])

print(varTypeDic.keys())

print(varTypeDic.values())

varTypeDic = dict([("key0", "value0"), ("key1", "value1")])
print(varTypeDic)

varTypeDic = dict(ek0=0, ek1="1", ek2="2")
print(varTypeDic)
varTypeDic.__contains__("none")
print(varTypeDic.__contains__("none"))