# !/usr/bin/python3

while True:
    try:
        x = int(input("请输入一个数字: "))
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
    else:
        print(x)
        break
    finally:
        print("finally")
        pass
