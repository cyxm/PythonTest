# !/usr/bin/python3

# 字符串类型
# 索引特性见列表类型

# 单引号和双引号等效
varTypeString0 = "hello"
varTypeString1 = 'world'
print(varTypeString0, varTypeString1)

# 三引号可在源码中换行
varTypeString2 = """this is multi line text
line0
line1"""
varTypeString3 = '''this is multi line text
line2
line3'''
print(varTypeString2)
print(varTypeString3)

# 使用\换行
varTypeString4 = "Hello" \
                 "World"
print(varTypeString4)

# r使\不转义
varTypeString5 = r"Yes/No\n"
print(varTypeString5)

# 级联字符串
varTypeString6 = "Connect""Multi""String"
print(varTypeString6)

# +运算
varTypeString7 = "Plus" + "Multi" + "String"
print(varTypeString7)

# *运算
varTypeString8 = "Multi" * 2 + "String"
print(varTypeString8)
