# !/usr/bin/python3

# 列表类型
# 列表中的元素是可变的

varTypeList = ["index0", 1, "2", 3, "index4", 5]
varTypeList1 = [0, "index1"]

# 输出完整列表
print(varTypeList)
# 输出列表第一个元素
print(varTypeList[0], end=" ")
# 从第二个开始输出到第三个元素
print(varTypeList[1:3], end=" ")
# 输出从第三个元素开始的所有元素
print(varTypeList[2:])

# 负索引
print(varTypeList[1:-1])

# 步进索引
print(varTypeList[0::2], end=" ")
print(varTypeList[-1::-2], end=" ")
# 翻转列表
print(varTypeList[-1::-1])

# 输出两次列表
print(varTypeList1 * 2, end=" ")
# 连接列表
print(varTypeList + varTypeList1)

# 删除索引位置的元素
# 错误示例,不能移除超出索引范围的元素
# del varTypeList[100]
# print(varTypeList)
del varTypeList[0]
print(varTypeList)

# 删除特定值的元素
# 错误示例,不能移除不存在的元素
# varTypeList.remove(2)
# print(varTypeList)
varTypeList.remove(1)
print(varTypeList)
