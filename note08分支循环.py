# i=0
# if(i==1):
#     print('1')
# elif(i==0):
#     print('0')
# print('end')
# j=1
# #1
# if(j==0):
#    if(i==0):
#        print(i)
# else:
#     print(j)
# #2
# if(j==1):
#    if(i==1):
#        print(i)
#    else:
#        print('2')
# #减少悬挂else，if由缩进匹配else，和其他语言不一样，
# #if由缩进匹配else
# #1的else与第一个if匹配，2与第二个if匹配
# #三元操作符
# b=True
# k=i if i<j else y#如果i<j k=j,否则k=j
# print(k)
# print('True') if i<j else print('false')
# #断言 assert 这个关键字为假的时候，程序自己崩溃，抛出AssertionError一场
# assert 4>3
# print('4>3')
# assert 3>4
# print('3>4')
soure=(int(input('请输入一个数')))
if(soure>=90):
    print('优秀')
elif(soure>=80):
    print('良好')
else:
    print('不及格')
#     悬挂else，但python使用强制的缩进，python代码会变得整洁，
if(4>5):
    if(4>5):
        print('4>5')
else:
    print('5')
#     三元操作符
x,y=4,5
small=x if x<y else y
print(small)
# 断言
# 错误的条件导致程序出现错误的结果，那就在出现错误的时候就让其死亡
assert 4>3
assert 3>4
