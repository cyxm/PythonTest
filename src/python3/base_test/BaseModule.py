# !/usr/bin/python3

# 导入包,会自动运行前置包中的__init__脚本
# import src.python3.base_test

# 导入包下所有模块
# 在windows下不工作,因为windows下文件名不区分大小写
# windows下使用此种方式需要在__init__中通过定义__all__变量指定模块名
# from src.python3.base_test import *
#
# print(BaseFunc.sameVar)

# 导入模块,需要使用全路径
# import src.python3.base_test.BaseFunc
#
# print(src.python3.base_test.BaseFunc.sameVar)
# src.python3.base_test.BaseFunc.test_func_dic("normal", index0="value0", index1="value1")
# clz = src.python3.base_test.BaseFunc.TestClz

# 导入模块,不需要前缀
# from src.python3.base_test.BaseFunc import *
#
# clz = TestClz
# test_func_dic("normal", index0="value0", index1="value1")
# print(sameVar)

# 导入模块,不需要包名前缀
# from src.python3.base_test import BaseFunc
#
# print(BaseFunc.sameVar)
# BaseFunc.test_func_dic("normal", index0="value0", index1="value1")
# clz = BaseFunc.TestClz
