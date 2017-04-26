# 汉诺塔
def hanoi(n, a='A', b='B', c='C'):
    if n == 1:
        print('move', a, '-->', c)
        return
    hanoi(n - 1, a, c, b)
    print('move', a, '-->', c)
    hanoi(n - 1, b, a, c)


print(hanoi(7))


def hanoi(n, a='A', b='B', c='C'):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)  # 将前n-1个盘子从A移动到B上
        print(a, '-->', c)  # 将最底下的最后一个盘子从a移动到C上
        hanoi(n - 1, b, a, c)  # 将b上的n-1盘子移动待c上
