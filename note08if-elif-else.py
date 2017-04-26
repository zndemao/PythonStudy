i=0
if(i==1):
    print('1')
elif(i==0):
    print('0')
print('e')
j=1
#1
if(j==0):
   if(i==0):
       print(i)
else:
    print(j)
#2
if(j==1):
   if(i==1):
       print(i)
   else:
       print('2')
#减少悬挂else，if由缩进匹配else，和其他语言不一样，
#if由缩进匹配else
#1的else与第一个if匹配，2与第二个if匹配
#三元操作符
b=True
k=i if i<j else y#如果i<j k=j,否则k=j
print(k)
print('True') if i<j else print('false')
#断言 assert 这个关键字为假的时候，程序自己崩溃，抛出AssertionError一场
assert 4>3
print('4>3')
assert 3>4
print('3>4')
