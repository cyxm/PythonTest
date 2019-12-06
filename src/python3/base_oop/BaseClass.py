# !/usr/bin/python3


class ClzBase:
    # 私有属性
    __privateMemInt = 45

    # 共有属性
    memInt = 34

    def __init__(self):
        print("__init__")
        pass

    def __del__(self):
        pass

    def funcTest(self):
        print("funcTest %d" % self.memInt)
        self.__privateFuncTest()
        pass

    def __privateFuncTest(self):
        print("private funcTest %d" % self.__privateMemInt)
        pass


class ClzAdv(ClzBase):

    def funcTest(self):
        super().funcTest()
        print("child print %s" % self.memInt)
        pass


clz = ClzAdv()

print(clz.memInt)
clz.funcTest()
