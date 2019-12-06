# !/usr/bin/python3

# 文件IO
filePath = r"e:\test\test.txt"

# 只读,文件必须存在,指针在开始
# file = open(filePath, "r")
#
# print(file.readline())
#
# file.close()

# 读写,文件必须存在,指针在开始
# file = open(filePath, "r+")
#
# file.writelines("begin")
# file.seek(0, 2)
# file.writelines("end")
# file.flush()
#
# file.seek(0)
# print(file.readline())
#
# file.close()

# 只写,文件不存在则创建文件,文件存在则覆盖文件,指针在开始
# file = open(filePath, "w")
#
# file.writelines("begin")
# file.seek(0, 2)
# file.writelines("end")
# file.flush()
#
# file.close()

# 读写,文件不存在则创建文件,文件存在则覆盖文件,指针在开始
# file = open(filePath, "w+")
#
# file.writelines("begin")
# file.seek(0, 2)
# file.writelines("end")
# file.flush()
#
# file.seek(0)
# print(file.readline())
#
# file.close()

# 只写,文件不存在则创建文件,文件存在打开原文件,指针在末尾
# file = open(filePath, "a")
#
# file.writelines("begin")
# file.writelines("end")
# file.flush()
#
# file.close()

# 读写,文件不存在则创建文件,文件存在打开原文件,指针在末尾
# file = open(filePath, "a+")
#
# file.writelines("begin")
# file.writelines("end")
# file.flush()
#
# file.seek(0)
# print(file.readline())
#
# file.close()
