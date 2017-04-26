Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class int(int):
	def __add__ (self,other):
		return int.__sub__(self,other)

	
>>> a=int('5')
>>> a
5
>>> b=int('3')
>>> b
3
>>> a+b
2
>>> 
=============================== RESTART: Shell ===============================
>>> class Nint(int):
	def __radd__(self,other):
		return int.__sub__ (self,other)

	
>>> a=Nint (5)
>>> b=Nint (3)
>>> a+b
8
>>> 1+b
2
>>> # ctrl + F6
>>> 
=============================== RESTART: Shell ===============================
>>> 
