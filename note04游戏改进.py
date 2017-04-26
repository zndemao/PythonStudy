import random
secret=random.randint(1,10)
print('-------第一个程序游戏改进---------')
temp=input('请输入一个数\t')
guess=int(temp)
while guess!=secret:
    temp=input('请输入一个数\t')
    guess=int(temp)
    if(guess==secret):
        print('true')
    else:
        if(guess>secret):
            print('大了')
        else:
            print('小了')
print('end')
