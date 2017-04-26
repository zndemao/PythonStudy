# 内嵌函数 or 闭包
# 内嵌函数
number = 10
number1 = 5


def MyFunction():
    number = 5
    print(number)
    global number1
    # 使用global 声明，才可在函数中修改全局变量
    number1 = 50
    print(number1)


MyFunction()
print(number)
print(number1)
print('内嵌函数'.center(20))


def Function():
    print('Function 被调用')

    def test():
        print('test 被调用')

    test()


Function()
print("闭包".center(20))


def FunX(x):
    def FunY(y):
        return x * y

    return FunY


i = FunX(8)
print(i)
print(type(i))
print(i(5))
print(FunX(5)(5))

print('python 2')


def Fun1():
    x = [5]

    def Fun2():
        x[0] *= x[0]
        return x[0]

    return Fun2()


print(Fun1())

print('python 3')


def Fun1():
    x = 5

    def Fun2():
        nonlocal  x
        x *= x
        return x

    return Fun2()


print(Fun1())
