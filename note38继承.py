Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 继承
>>> # class  DerivedClassName(BaseClassName):
>>> class Parent:
	def hollo(self):
		print('zahng zai diao yong fu lei fang fa ')

		
>>> class Child(Parent):
	pass

>>> p=Parent ()
>>> p.hollo()
zahng zai diao yong fu lei fang fa 
>>> c =Child ()
>>> c.hollo()
zahng zai diao yong fu lei fang fa 
>>> class Child(Parent):
	def hollo(self):
		print('zahng zai diao yong zi lei fang fa ')

		
>>> c=Child ()
>>> c.hollo()
zahng zai diao yong zi lei fang fa 
>>> p=Parent ()
>>> p.hollo()
zahng zai diao yong fu lei fang fa 
>>> 
