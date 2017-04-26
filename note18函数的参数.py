# 参数
# 形参 实参
def MyFirstFunction(name):  # name 形参
    '函数定义过程中的name是形参'
    print(name)


MyFirstFunction('小姐姐')  # '小姐姐' 实参

print(MyFirstFunction.__doc__)
help(MyFirstFunction)


# print(print.__doc__)
# 关键字参数
def SaySome(name, words):
    print(name + words)


SaySome('name', '123')
# 关键字索引参数
SaySome(words='123', name='name')


# 关键字参数，与默认参数
def SaySome(name='zn', words='cat'):
    print(name + words)


SaySome()
SaySome('name')


# 收集参数
def test(*params):
    print(len(params))
    print(params[1])


test(1, 3, 4, 5, 6, 73, 42, 4)
