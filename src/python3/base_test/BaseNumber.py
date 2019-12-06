# !/usr/bin/python3

# 基本数字类型

# 布尔
# 在Python2中没有布尔型,用数字 0 表示 False，用 1 表示 True
# 在Python3中,True 和 False 定义成了关键字,但它们的值还是1和0,它们可以和数字相加
varTypeBoolTrue = True
varTypeBoolFalse = False

if varTypeBoolTrue:
    print("bool true =", varTypeBoolTrue)

if not varTypeBoolFalse:
    print("bool false =", varTypeBoolFalse)

# 整数
varTypeInt = 100
print(varTypeInt, end=" ")

# 8进制
varTypeInt = 0o20
print(varTypeInt, end=" ")

# 16进制
varTypeInt = 0x20
print(varTypeInt)

# 浮点
varTypeFloat = 2.05
print(varTypeFloat, end=" ")

varTypeFloat = 14.36E-2
print(varTypeFloat)

# 复数
varTypeComplex = 1.2 + 2.6j
print(varTypeComplex, end=" ")

varTypeComplex *= 2.3 - 1.5j
print(varTypeComplex, end=" ")

varTypeComplex = 3e5j
print(varTypeComplex)

# 数值运算

# 加法
varCal = 6 + 9
print(varCal, end=" ")

# 减法
varCal = 7 - 2
print(varCal, end=" ")

# 乘法
varCal = 5 * 9
print(varCal, end=" ")

# 整数除法
varCal = 46 // 5
print(varCal, end=" ")

# 整数取余
varCal = 46 % 5
print(varCal, end=" ")

# 浮点除法
varCal = 46 / 5
print(varCal, end=" ")

# 乘方
varCal = 2 ** 4
print(varCal)
