Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print
<built-in function print>
>>> print('1')
1
>>> print '1'#python3中不能使用，python2中正确
SyntaxError: Missing parentheses in call to 'print'
>>> print("34")
34
>>> print(3+8)
11
>>> 1234567890*123456789
152415787501905210
>>> print('i'+'love')
ilove
>>> print('i'*8)
iiiiiiii
>>> print('love\n'*7)
love
love
love
love
love
love
love

>>> print('love'+4)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print('love'+4)
TypeError: must be str, not int
>>> 
