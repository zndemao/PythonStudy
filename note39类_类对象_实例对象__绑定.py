Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Mixin编程机制
>>> # 类 类对象，实例对象
>>> class C:
	count = 0

	
>>> a=C()
>>> b=C()
>>> c=C()
>>> a.count
0
>>> b.count
0
>>> c.count
0
>>> c.count+=10
>>> c.count
10
>>> a.count
0
>>> b.count
0
>>> c.count
10
>>> C.count
0
>>> C.count+=100
>>> a.count
100
>>> b.count
100
>>> c.c
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c.c
AttributeError: 'C' object has no attribute 'c'
>>> c.count
10
>>> class B :
	def x(self):
		print('x')

		
>>> B=B()
>>> B.x()
x
>>> c.x=1
>>> c.x
1
>>> B.x=1
>>> B.x
1
>>> B.x()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    B.x()
TypeError: 'int' object is not callable
>>> # 绑定
>>> class Aa:
	def printAa()::
		
SyntaxError: invalid syntax
>>> class Aa:
	def printAa():
		print('aa')

		
>>> Aa.printAa()
aa
>>> aa=Aa()
>>> aa.printAa()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    aa.printAa()
TypeError: printAa() takes 0 positional arguments but 1 was given
>>> aa.printAa(aa)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    aa.printAa(aa)
TypeError: printAa() takes 0 positional arguments but 2 were given
>>> class CC:
	def setXY(self ,x,y):
		self .x=x
		self.y=y
	def printXY(self):
		print(self.x,self.y)

		
>>> dd==CC()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dd==CC()
NameError: name 'dd' is not defined
>>> dd=CC()
>>> dd.__dict__
{}
>>> CC.__dict__
mappingproxy({'__module__': '__main__', 'setXY': <function CC.setXY at 0x00650930>, 'printXY': <function CC.printXY at 0x00650978>, '__dict__': <attribute '__dict__' of 'CC' objects>, '__weakref__': <attribute '__weakref__' of 'CC' objects>, '__doc__': None})
>>> dd.setXY (4,5)
>>> dd.__dict__
{'x': 4, 'y': 5}
>>> CC.__dict__
mappingproxy({'__module__': '__main__', 'setXY': <function CC.setXY at 0x00650930>, 'printXY': <function CC.printXY at 0x00650978>, '__dict__': <attribute '__dict__' of 'CC' objects>, '__weakref__': <attribute '__weakref__' of 'CC' objects>, '__doc__': None})
>>> del CC
>>> ee = CC()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    ee = CC()
NameError: name 'CC' is not defined
>>> dd.printXY()
4 5
>>> 
