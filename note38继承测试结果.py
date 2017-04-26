Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note39继承测试.py ===========
>>> fish =Fish()
>>> fish .move()
weizi -1 4
>>> fish .move()
weizi -2 4
>>> go=GoldFish()
>>> go.move()
weizi 6 0
>>> go.move()
weizi 5 0
>>> shark=Shark()
>>> shark.eat()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    shark.eat()
  File "E:/Users/zxl96/Documents/python/note39继承测试.py", line 26, in eat
    if self.hungry:
AttributeError: 'Shark' object has no attribute 'hungry'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note39继承测试.py ===========
>>> shark=Shark()
>>> shark.eat()
吃货的梦想是天天吃
>>> shark.move()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    shark.move()
  File "E:/Users/zxl96/Documents/python/note39继承测试.py", line 9, in move
    self.x -= 1
AttributeError: 'Shark' object has no attribute 'x'
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note39继承测试.py ===========
>>> shark=Shark()
>>> shark.move()
weizi 7 1
>>> shark.move()
weizi 6 1
>>> Fish.__init__(shark)
>>> shark .move()
weizi 5 1
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note39继承测试.py ===========
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note39继承测试.py ===========
>>> shark=Shark()
>>> shark.move()
weizi 5 4
>>> 
