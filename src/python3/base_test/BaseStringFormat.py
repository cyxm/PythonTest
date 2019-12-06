# !/usr/bin/python3

# 格式化
print("字符 %c" % "s")
print("字符串 %s,%s" % ("String", "Example"))

print("整数:%d" % 23, end=" ")
print("整数:%+d" % 23, end=" ")
print("整数:%04d" % 23, end=" ")
print("整数:% 4d" % 23, end=" ")

print("整数 %u" % 12)

print("8进制:%o" % 16, end=" ")
print("8进制:%#o" % 16, end=" ")
print("16进制:%x" % 46, end=" ")
print("16进制:%#x" % 46, end=" ")
print("16进制:%X" % 46, end=" ")
print("16进制:%#X" % 46)

print("浮点:%f" % 5.0255, end=" ")
print("浮点:%.3f" % 5.0255, end=" ")
print("浮点:%.3f" % 5.0254)

print("科学计数法 %e" % 52000)
print("科学计数法 %E" % 52000)
print("科学计数法 %e" % 0.0025)
