Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 魔法方法总是被双下划线包围，例如__init__
>>> # 魔法方法是面对对象的Python的一切，
>>> # 体现在他们总能够在适当的时候被自动调用
>>> # __init__(self[ , ...])
>>> class Rectangle:
	def __init__ (self ,x,y):
		self.x=x
		self.y=y
	def getPeri(self):
		return (self.x+self.y)*2
	def getArea(self):
		return (self.x*self.y)

	
>>> rect=Rectangle (3,4)
>>> rect .getPeri()
14
>>> rect .getArea ()
12
>>> class A:
	def __init__(self):
		return "a for A-cup"

	
>>> a=A()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a=A()
TypeError: __init__() should return None, not 'str'
>>> # __new__(cls9, ...]) 第一个被调用的方法
>>> class CapStr(str):
	def __new__(cls,string):
		string=string.upper()
		return str.__new__(cls,string)

	
>>> a=CapStr('L Love')
>>> a
'L LOVE'
>>> # __del__(self) 将对象要被销毁时，自动调用，垃圾回收机制自动把他销毁
>>> class C:
	def __init__(self):
		print('init')
	def __del__(self):
		print('del')

		
>>> c1=C()
init
>>> c2=c1
>>> c3=c2
>>> del c3
>>> del c2
>>> del c1
del
>>> 
