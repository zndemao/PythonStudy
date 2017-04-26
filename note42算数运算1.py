Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type (len)
<class 'builtin_function_or_method'>
>>> type (dir)
<class 'builtin_function_or_method'>
>>> type (int)
<class 'type'>
>>> type (list)
<class 'type'>
>>> class New_int(int):
	def __add__(self,other):
		return int.__sub__ (self,other)
	def __sub__(self,other):
		return int.__add__ (self,other)

	
>>> a=New_int(3)
>>> b=New_int(4)
>>> a+b
-1
>>> a-b
7
>>> class Try_int(int):
	def __add__(self,other ):
		return self+other
	def __sub__(self,other ):
		return self-other

	
>>> a=Try_int (3)
>>> b=Try_int (5)
>>> a+b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a+b
  File "<pyshell#14>", line 3, in __add__
    return self+other
  File "<pyshell#14>", line 3, in __add__
    return self+other
  File "<pyshell#14>", line 3, in __add__
    return self+other
  [Previous line repeated 327 more times]
RecursionError: maximum recursion depth exceeded while calling a Python object
>>> class Try_int(int):
	def __add__(self,other ):
		return int(self) + int(other)
	def __sub__(self,other ):
		return int(self) - int(other)

	
>>> a=Try_int (3)
>>> a=Try_int (5)
>>> a+b
10
>>> a=Try_int (3)
>>> b=Try_int (3)
>>> a+b
6
>>> 
