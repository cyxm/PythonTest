# !/usr/bin/python3

# 集合类型
# 包含的元素不可重复
# 可以进行集合运算

# 集合为无序
varTypeSet = {"0", "1", "2", "3"}
varTypeSet1 = {"2", "3", "4", "5"}
print(varTypeSet, varTypeSet1)

# 差集
print("差集", end=" ")
print(varTypeSet - varTypeSet1, end=" ")
print(varTypeSet1 - varTypeSet)

# 并集
# 错误示例,不能使用+
# print(varTypeSet + varTypeSet1)
print("并集", end=" ")
print(varTypeSet | varTypeSet1)

# 交集
print("交集", end=" ")
print(varTypeSet & varTypeSet1)

# 差集的并集
print("差集的并集", end=" ")
print(varTypeSet ^ varTypeSet1)
