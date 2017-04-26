# python 递归深度为一百层
import sys

sys.setrecursionlimit(1000)  # 设置递归深度


# 非递归版本
def Factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print('阶乘是', Factorial(5))


# 递归版本
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
# 调用自身，有返回条件
