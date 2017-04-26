Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 迭代
>>> for i in "cat":
	print(i)

	
c
a
t
>>> links={'bili':'http://www.bilibili.com',\
       'ingerss':'xuedingedemao'}
>>> for each in links:
	print('%s-->%s'%(each,links[each]))

	
bili-->http://www.bilibili.com
ingerss-->xuedingedemao
>>> # iter()	next()
>>> string ='cat'
>>> it= iter(string)
>>> next(it)
'c'
>>> next(it)
'a'
>>> next(it)
't'
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    next(it)
StopIteration
>>> string = 'cat'
>>> it=iter(string)
>>> while True:
	try :
		each =next(it)
	except StopIteration :
		break
	print(each)

	
c
a
t
>>> # 魔法方法 __iter__()	__next__()
>>> # 迭代器
>>> class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

>>> fibs=Fibs ()
>>> for each in fibs :
	print(each)

	
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    print(each)
KeyboardInterrupt
>>> fibs=Fibs ()
>>> for each in fibs :
	if each<20:
		print(each)
	else :
		break

	
1
1
2
3
5
8
13
>>> class Fibs:
    def __init__(self, n=10):
        self.a = 0
        self.b = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a

>>> fibs=Fibs ()
>>> for each in fibs :
	print(each)

	
1
1
2
3
5
8
>>> fibs=Fibs (100)
>>> for each in fibs :
	print(each)

	
1
1
2
3
5
8
13
21
34
55
89
>>> 
