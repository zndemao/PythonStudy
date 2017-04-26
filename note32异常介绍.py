Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my = ['cat']
>>> assert len(my)>0
>>> my.pop()
'cat'
>>> assert len(my)>0
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    assert len(my)>0
AssertionError
>>> my.fishc#未知的对象方法
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    my.fishc#未知的对象方法
AttributeError: 'list' object has no attribute 'fishc'
>>> my=[1,2,30]
>>> my[3]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    my[3]
IndexError: list index out of range
>>> my[2]
30
>>> my_dict={'one':1,'two':2}
>>> my_dict['one']
1
>>> my_dict['three']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    my_dict['three']
KeyError: 'three'
>>> my_dict.get('four')
>>> i
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    i
NameError: name 'i' is not defined
>>> #OSError
>>> print 'love'
SyntaxError: Missing parentheses in call to 'print'
>>> #python 2时可以，3不可以
>>> 1+'1'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    1+'1'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 3/1
3.0
>>> 10//3
3
>>> 10/3
3.3333333333333335
>>> 10/0
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
>>> 
