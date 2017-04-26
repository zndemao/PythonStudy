Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 生成器
>>> def myGen():
	print('生成器被执行')
	yield 1
	yield 2

	
>>> myG=myGen()
>>> next(myG)
生成器被执行
1
>>> next(myG)
2
>>> next(myG)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    next(myG)
StopIteration
>>> for i in myGen ():
	print(i)

	
生成器被执行
1
2
>>> def libs():
	a=0
	b=1
	while True:
		a,b =b,a+b
		yield a

		
>>> for each in libs():
	if each >100:
		break
	print(each ,end=' ')

	
1 1 2 3 5 8 13 21 34 55 89 
>>> a =[i for i in range(100) if not (i%2) and i%3]
>>> a
[2, 4, 8, 10, 14, 16, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52, 56, 58, 62, 64, 68, 70, 74, 76, 80, 82, 86, 88, 92, 94, 98]
>>> b = {i:i % 2==0 for i in range(10)}
>>> b
{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
>>> c ={i for i in [1,1,3,5,3,545,3,34,6553,2,2,4]}
>>> c
{1, 34, 3, 545, 5, 2, 4, 6553}
>>> d= "i for i in 'cat'"
>>> d
"i for i in 'cat'"
>>> e =(i for i in range(10))
>>> e
<generator object <genexpr> at 0x0407FAE0>
>>> next(e)
0
>>> next(e)
1
>>> next(e)
2
>>> for each in e:
	print (each)

	
3
4
5
6
7
8
9
>>> 
>>> sum ((i for i in range(100) if i%2))
2500
>>> 
