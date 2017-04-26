i=0
while(True):
    number=int(input('qingshuru'))
    if(i==number):
        break
print('end')
favourite = "fishC"
for i in favourite:
    print(i, end=" ")
print('end \n')
#  列表，相当于数组
array = ['1', '2', '3', '4']
for i in array:
    print(i, end=" ")
# range() range([strat] stop[,stop=1])
# range这个BIF的主要作用是商城一个从start参数值开始到stop参数值结束的数字序列
range(0, 5)
list(range(0, 5))
for i in range(5):
    print(i)
for i in range(2, 9):
    print(i)
for i in range(1, 10, 2):  # 第三个参数是步进，例如每次累加
    print(i)
for i in range(0, 100, 10):
    print(i)
while (True):
    print('true')
    break
while True:
    print(1)
    break
for i in range(10):
    if i%2 !=0:
        print(i)
        continue
    i+=2
    print(i)
#循环中同样有break 和continue ，for 和 for in 一起使用 range() bif的使用
# 同时发现待（） 和不带（）效果一样，
i=0
if i==0:
    print(i)
if (i==0):
    print(i)
