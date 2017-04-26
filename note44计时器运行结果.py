Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class A():
    def __str__(self):
        return 'cat'

>>> a =A()
>>> a
<__main__.A object at 0x03046C70>
>>> class B():
    def __repr__(self):
        return 'cat'

>>> b=B()
>>> b
cat
>>> print(a)
cat
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start ()
start timer
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop ()
run time 000008
timer stop
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop ()
timer stop
>>> t1
run time 000003
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1
no start timer
>>> t1.start()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t1.start()
TypeError: 'int' object is not callable
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1
no start timer
>>> t1.start ()
start timer
>>> t1.stop ()
timer stop
>>> t1
run time 000009
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start ()
start timer
>>> t1.stop ()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t1.stop ()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 25, in stop
    self.__calc()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 34, in __calc
    if lasted == 0:
NameError: name 'lasted' is not defined
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start ()
start timer
>>> t1.stop
<bound method MyTimer.stop of no start timer>
>>> t1.stop()
timer stop
>>> t1
run time 
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start ()
start timer
>>> t1.stop ()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t1.stop ()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 25, in stop
    self.__calc()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 35, in __calc
    self.prompt += str(self.lasted[index]+self.unit[index])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t1.stop()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 25, in stop
    self.__calc()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 35, in __calc
    self.prompt += str(self.lasted[index]+self.unit[index])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t1.stop()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 25, in stop
    self.__calc()
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 35, in __calc
    self.prompt += str(self.lasted[index]+self.unit[index])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
SyntaxError: invalid syntax
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> 
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop()
timer stop
>>> t1
run time 5秒
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1
no start timer
>>> t1.start()
start timer
>>> t1
请先调用stop（） 停止计时
>>> t1.stop()
timer stop
>>> t1
run time 12秒
>>> t1.stop()
timer stop
>>> t1
run time 26秒
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1
no start timer
>>> t1.start()
start timer
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1
no start timer
>>> t1.stop()
>>> t1
start（） start计时
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.stop()
请先调用start（） start计时
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop()
timer stop
>>> t1
run time 6秒
>>> t2=MyTimer()
>>> t2.start()
start timer
>>> t2.stop()
timer stop
>>> t2
run time 4秒
>>> t1+t2
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    t1+t2
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 21, in __add__
    result.appnd (self.lasted[index] - other.lasted[index])
AttributeError: 'list' object has no attribute 'appnd'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop()
timer stop
>>> t2.MyTimer()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t2.MyTimer()
NameError: name 't2' is not defined
>>> t2=MyTimer()
>>> t2.start()
start timer
>>> t2.stop()
timer stop
>>> t1
run time 1分钟-54秒
>>> t2
run time 6秒
>>> t1+t2
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    t1+t2
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 21, in __add__
    result.appnd (self.lasted[index] + other.lasted[index])
AttributeError: 'list' object has no attribute 'appnd'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop()
timer stop
>>> t1
run time 1分钟-53秒
>>> t2=MyTimer()
>>> t2.start()
start timer
>>> tw2.stop()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    tw2.stop()
NameError: name 'tw2' is not defined
>>> t2.stop()
timer stop
>>> t2
run time 13秒
>>> t1+t2
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    t1+t2
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 21, in __add__
    result.appnd (self.lasted[index] + other.lasted[index])
AttributeError: 'list' object has no attribute 'appnd'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start ()
start timer
>>> t1.stop()
timer stop
>>> t1
run time 4秒
>>> t2=MyTimer()
>>> t2.start()
start timer
>>> t2.stop()
timer stop
>>> t2
run time 4秒
>>> t1+t2
self.lasted[index] 0
other.lasted[index 0
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    t1+t2
  File "E:/Users/zxl96/Documents/python/note44计时器.py", line 23, in __add__
    result.appnd(self.lasted[index] + other.lasted[index])
AttributeError: 'list' object has no attribute 'appnd'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note44计时器.py ===========
>>> t1=MyTimer()
>>> t1.start()
start timer
>>> t1.stop()
timer stop
>>> t1
run time 1分钟-55秒
>>> t2=MyTimer()
>>> t2.start()
start timer
>>> t2.stop()
timer stop
>>> t1+t2
self.lasted[index] 0
other.lasted[index 0
self.lasted[index] 0
other.lasted[index 0
self.lasted[index] 0
other.lasted[index 0
self.lasted[index] 0
other.lasted[index 0
self.lasted[index] 1
other.lasted[index 0
self.lasted[index] -55
other.lasted[index 4
'总共运行了1分钟-51秒'
>>> t2
run time 4秒
>>> 
