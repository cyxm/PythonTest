# !/usr/bin/python3

import re

str0 = "begin_end"

# 只从起始位置开始匹配
pattern = re.compile("begin")
matchRet = pattern.match(str0)
if matchRet:
    print(matchRet.span(), end=" ")
    print(matchRet.group())
else:
    print("not match")

pattern = re.compile("end")
matchRet = pattern.match(str0)
if matchRet:
    print(matchRet.span())
else:
    print("not match")

# 全文匹配并返回一次
pattern = re.compile("end")
matchRet = pattern.search(str0)
if matchRet:
    print(matchRet.span(), end=" ")
    print(matchRet.group())
else:
    print("not match")

