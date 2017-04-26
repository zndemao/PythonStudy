# 函数 与 过程
# 函数:有返回值
# 过程:没有返回值
# Python只用函数没有过程
def hello():
    print('hello world')


temp = hello()
print(type(temp))


# 有返回值，返回返回值，没有返回NoneType

def back():
    return [1, 'love', 3.14]


print(back())


# 函数变量的作用域
def discounts(price, rate):
    final_price = price * rate
    # print(old_price)
    old_price = 200
    print(old_price)
    return final_price


old_price = float(input('请输入'))
rate = float(input('请输入折扣率'))
new_price = discounts(old_price, rate)
print('打折后的价格' + str(new_price))
# 不能使用+ 二者无法进行算数运算
print("打折后的价格", new_price)
# print('这里试图打印final_price的值:',final_price)
# 局部变量，出来函数无效
print(old_price)
# 如果在函数内如果试图修改全局变量，python会创建一个局部变量，名字虽然相同
