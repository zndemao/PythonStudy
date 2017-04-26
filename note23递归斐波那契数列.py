# 0.618 or 1:1.618
def factorial1(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print('输入有错')
        return -1
    while (n - 2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3


print(factorial1(8))
print(factorial1(30))
print(factorial1(40))


def factorial2(n):
    if n < 1:
        print('输入有误')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return factorial2(n - 1) + factorial2(n - 2)


print(factorial2(8))
# 分治思之
print(factorial2(30))
print(factorial2(40))

