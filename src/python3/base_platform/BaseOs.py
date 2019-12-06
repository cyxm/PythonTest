# !/usr/bin/python3

import os
import sys

filePath = r"e:\test\test.txt"

ret = os.access(filePath, os.F_OK)
print("路径是否存在 %s" % ret)

ret = os.access(filePath, os.R_OK)
print("可读 %s" % ret)

ret = os.access(filePath, os.W_OK)
print("可写 %s" % ret)

ret = os.access(filePath, os.X_OK)
print("可执行 %s" % ret)

print("平台 %s" % sys.platform)
