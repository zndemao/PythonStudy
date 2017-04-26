Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 多重继承
>>> class Base1:
	def fool(self):
		print('fool')

		
>>> class Base2:
	def foo2(self):
		print('foo2')


>>> class C(Base1 ,Base2 ):
	pass

>>> c=C()
>>> c.fool ()
fool
>>> c.foo2()
foo2
>>> 
