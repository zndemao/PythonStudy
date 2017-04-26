Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Ball:
	def setName(self ,name):
		self.name=name
	def kick(self):
		print('该死的谁踢我....%d' ,  self.name)

		
>>> a=Ball()
>>> a.setName('A')
>>> a.kick ()
该死的谁踢我....%d A
>>> b=Ball()
>>> b.setName('b')
>>> c=Ball()
>>> c.setName('c')
>>> b.kick()
该死的谁踢我....%d b
>>> # 什么 self
>>> # _init_(self)
>>> class Ball:
	def __init__(self, name):
		self.name=name
	def kick(self):
		print('该死的谁踢我....%d' ,  self.name)

		
>>> b=Ball('cat')
>>> b.kick()
该死的谁踢我....%d cat
>>> c = Ball()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c = Ball()
TypeError: __init__() missing 1 required positional argument: 'name'
>>> class cat :
	name='tom'

	
>>> p =cat()
>>> p.name
'tom'
>>> # name manfling 名字改编，名字重整
>>> # python 中定义私有变量只需要在变量名或者函数名前加上‘__'两个下划线
>>> # 那么这个函数或变量就会为私有的了
>>> class cat :
	name='tom'
	__age=1

	
>>> p=cat()
>>> p.name
'tom'
>>> p.__age
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    p.__age
AttributeError: 'cat' object has no attribute '__age'
>>> class Cat :
	name='tom'
	__age=1
	def getName(self):
		return self.__age

	
>>> c=Cat()
>>> c.__age
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c.__age
AttributeError: 'Cat' object has no attribute '__age'
>>> c.getName()
1
>>> c._Cat__age
1
>>> 
