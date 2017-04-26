# 自己引入异常
raise ZeroDivisionError('0')


try:
    # 检测范围
    # int('abc')
    sun = 1 + '1'
    f = open('not_test.txt')
    f.close()
except (OSError, TypeError):
    print('error')
finally:
    print('end')

# 和其他语言一样
