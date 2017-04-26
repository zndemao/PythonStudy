Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py ======
>>> r1=Rectangle ()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    r1=Rectangle ()
  File "E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py", line 3, in __init__
    self.width = width
  File "E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py", line 11, in __setattr__
    self.key = value
  File "E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py", line 11, in __setattr__
    self.key = value
  File "E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py", line 11, in __setattr__
    self.key = value
  [Previous line repeated 325 more times]
  File "E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py", line 7, in __setattr__
    if key == 'square':
RecursionError: maximum recursion depth exceeded in comparison
>>> 
====== RESTART: E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py ======
>>> r1=Rectangle ()
>>> r1=Rectangle (4.5)
>>> r1.getArea()
0.0
>>> 
====== RESTART: E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py ======
>>> r1=Rectangle (4.5)
>>> r1.getArea()
0.0
>>> 
====== RESTART: E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py ======
>>> r1=Rectangle (4.5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    r1=Rectangle (4.5)
  File "E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py", line 3, in __init__
    self.width = width
  File "E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py", line 7, in __setattr__
    if key == 'square':
NameError: name 'key' is not defined
>>> 
====== RESTART: E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py ======
>>> r1=Rectangle (4.5)
>>> r1.getArea
<bound method Rectangle.getArea of <__main__.Rectangle object at 0x0353AB30>>
>>> r1.getArea()
0.0
>>> r1.width
4.5
>>> r1=Rectangle (4,5)
>>> r1.getArea()
20
>>> r1.square=10
>>> r1.width
10
>>> r1.getArea()
100
>>> r1.__dict__
{'width': 10, 'height': 10}
>>> 
====== RESTART: E:/Users/zxl96/Documents/python/note45Rectangle举例测试.py ======
>>>  r1=Rectangle (4,5)
 
SyntaxError: unexpected indent
>>> r1=Rectangle (4,5)
>>> r1.getArea()
20
>>> r1.square=10
>>> r1.getArea()
100
>>> r1.__dict__
{'width': 10, 'height': 10}
>>> 
