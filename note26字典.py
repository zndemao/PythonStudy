Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1={}
>>> dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict1.fromkeys((1,2,3),'number')
{1: 'number', 2: 'number', 3: 'number'}
>>> dict1.fromkeys((1,2,3),('one','two','three'))
{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
>>> dict1.fromkeys((1,3),'数字')
{1: '数字', 3: '数字'}
>>> # keys() ,values() ,items()
>>> dict1=dict1.fromkeys((range(32)),'暂')
>>> 
>>> dict1
{0: '暂', 1: '暂', 2: '暂', 3: '暂', 4: '暂', 5: '暂', 6: '暂', 7: '暂', 8: '暂', 9: '暂', 10: '暂', 11: '暂', 12: '暂', 13: '暂', 14: '暂', 15: '暂', 16: '暂', 17: '暂', 18: '暂', 19: '暂', 20: '暂', 21: '暂', 22: '暂', 23: '暂', 24: '暂', 25: '暂', 26: '暂', 27: '暂', 28: '暂', 29: '暂', 30: '暂', 31: '暂'}
>>> for eachkey in dict1.keys():
	print(eachkey)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
>>> for eachkey in dict1.valus():
	print(eachkey)

	
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for eachkey in dict1.valus():
AttributeError: 'dict' object has no attribute 'valus'
>>> for eachkey in dict1.values():
	print(eachkey)

	
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
暂
>>> for eachkey in dict1.items():
	print(eachkey)

	
(0, '暂')
(1, '暂')
(2, '暂')
(3, '暂')
(4, '暂')
(5, '暂')
(6, '暂')
(7, '暂')
(8, '暂')
(9, '暂')
(10, '暂')
(11, '暂')
(12, '暂')
(13, '暂')
(14, '暂')
(15, '暂')
(16, '暂')
(17, '暂')
(18, '暂')
(19, '暂')
(20, '暂')
(21, '暂')
(22, '暂')
(23, '暂')
(24, '暂')
(25, '暂')
(26, '暂')
(27, '暂')
(28, '暂')
(29, '暂')
(30, '暂')
(31, '暂')
>>> print(dict1(32))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(dict1(32))
TypeError: 'dict' object is not callable
>>> print(dict1(31))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(dict1(31))
TypeError: 'dict' object is not callable
>>> print(dict1[31])
暂
>>> print(dict1[32])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(dict1[32])
KeyError: 32
>>> #试图访问不存在的项
>>> print(dict1.get(32))
None
>>> print(dict1.get(32),'没有')
None 没有
>>> dict1.get(32),'没有'
(None, '没有')
>>> dict1.get(32,'木有')
'木有'
>>> dict1.get(31,'木有')
'暂'
>>> 31 in dict1
True
>>> 32 in dict1
False
>>> dict1
{0: '暂', 1: '暂', 2: '暂', 3: '暂', 4: '暂', 5: '暂', 6: '暂', 7: '暂', 8: '暂', 9: '暂', 10: '暂', 11: '暂', 12: '暂', 13: '暂', 14: '暂', 15: '暂', 16: '暂', 17: '暂', 18: '暂', 19: '暂', 20: '暂', 21: '暂', 22: '暂', 23: '暂', 24: '暂', 25: '暂', 26: '暂', 27: '暂', 28: '暂', 29: '暂', 30: '暂', 31: '暂'}
>>> dict1.clear()
>>> dict1
{}
>>> dict1={}
>>> dict1
{}
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> a={1;'one',2:'two'}
SyntaxError: invalid syntax
>>> a={1:'one',2:'two'}
>>> b=a.copy()
>>> c=a
>>> c
{1: 'one', 2: 'two'}
>>> b
{1: 'one', 2: 'two'}
>>> a
{1: 'one', 2: 'two'}
>>> id(a)
53885376
>>> id(b)
53485808
>>> id(c)
53885376
>>> c[3]='three'
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> a
{1: 'one', 2: 'two', 3: 'three'}
>>> b
{1: 'one', 2: 'two'}
>>> a.pop(2)
'two'
>>> a
{1: 'one', 3: 'three'}
>>> a,propertyitem()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a,propertyitem()
NameError: name 'propertyitem' is not defined
>>> a.popitem ()
(3, 'three')
>>> a.setdefault('小白')
>>> a
{1: 'one', '小白': None}
>>> a.setdefault(4,'小白')
'小白'
>>> a
{1: 'one', '小白': None, 4: '小白'}
>>> #字典随机排序
>>> b={'小白':'cat'}
>>> a.updata(b)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.updata(b)
AttributeError: 'dict' object has no attribute 'updata'
>>> a.update(b)
>>> a
{1: 'one', '小白': 'cat', 4: '小白'}
>>> 
