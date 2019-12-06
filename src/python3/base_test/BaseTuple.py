# !/usr/bin/python3

# 元组和列表类似,但其中的元素不可改变

# 空元组
varTypeTuple = ()
print(varTypeTuple)

# 单元素,需要在元素后添加逗号,否则不被视为元组
# 错误示例
# varTypeTuple = (20)
# print(isinstance(varTypeTuple, tuple))
varTypeTuple = (20,)
print(isinstance(varTypeTuple, tuple))
print(varTypeTuple)
