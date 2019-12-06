# !/usr/bin/python3


def test_func(normal_str, key_str, default_str="default"):
    """

    :param normal_str:
    :param key_str:
    :param default_str:
    :return:
    """
    print(normal_str, end=" ")
    print(key_str, end=" ")
    print(default_str)
    pass


def test_func_tuple(normal_str, default_str="default", *args):
    print(normal_str, end=" ")
    print(default_str, end=" ")
    print(args)
    pass


def test_func_tuple1(normal_str, *args, default_str="default"):
    print(normal_str, end=" ")
    print(default_str, end=" ")
    print(args)
    pass


def test_func_dic(normal_str, **kwargs):
    print(normal_str)
    print(kwargs)
    pass


class TestClz:
    def mem_func(self):
        pass


sameVar = "sameVar=func"

if __name__ == "__main__":
    test_func("normal", key_str="key")

    test_func_tuple("index0", "index1", "index2")
    test_func_tuple1("index0", "index1", "index2")

    test_func_dic("normal", index0="value0", index1="value1")
    pass

