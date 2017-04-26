class Cat:  # python 中的类名约定以大写字母开头
    '''关于类的简单例子'''
    # 属性
    color = 'back'
    weight = 10
    age = 1

    # 方法
    def shuijiao(self):
        print('睡觉')

    def chi(self):
        print('chi')

    def meng(self):
        print('卖萌')


tt = Cat()
tt.chi()
tt.meng()
# 封装
list1 = [2, 543, 25, 2, 5]
list1.sort()
print(list1)
list1.append(9)
print(list1)


# 继承
class MyList(list):
    pass


list2 = MyList()
list2.append(5)
list2.append(3)
list2.append(4)
list2.append(2)
print(list2)
list2.sort()
print(list2)


# 多态
class A:
    def fun(self):
        print('A')


class B:
    def fun(self):
        print('b')


a = A()
b = B()
a.fun()
b.fun()
