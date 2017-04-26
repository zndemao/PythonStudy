Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class MyDecriptor:
    def __get__(self, instance, owner):
        print('__get__', self, instance, owner)

    def __set__(self, instance, value):
        print('__set__', self, instance, value)

    def __delete__(self, instance):
        print("__delete__", instance)

        
>>> class Test:
	x=MyDecriptor()

	
>>> test=Test()
>>> test.x
__get__ <__main__.MyDecriptor object at 0x01376C70> <__main__.Test object at 0x0363AB30> <class '__main__.Test'>
>>> test
<__main__.Test object at 0x0363AB30>
>>> Test
<class '__main__.Test'>
>>> test.x="x-man"
__set__ <__main__.MyDecriptor object at 0x01376C70> <__main__.Test object at 0x0363AB30> x-man
>>> del test.x
__delete__ <__main__.Test object at 0x0363AB30>
>>> 
=============================== RESTART: Shell ===============================
>>> class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __del__(self, instance):
        self.__del__(instance)

        
>>> class C:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, valus):
        self._x = valus

    def delX(self):
        del self._x

    x = MyProperty(getX, setX, delX)

    
>>> c=C()
>>> c.x
>>> c.x='x'
>>> c.x
'x'
>>> del c.x
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    del c.x
AttributeError: __delete__
>>> 
=============================== RESTART: Shell ===============================
>>> # 定义一个温度类
>>> 
=========== RESTART: E:/Users/zxl96/Documents/python/note47温度举例.py ===========
>>> temp=Temperature()
>>> temp.cel
26.0
>>> temp=Temperature (30)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    temp=Temperature (30)
TypeError: object() takes no parameters
>>> temp.cel=30
>>> temp.fah
86.0
>>> temp.fah=100
>>> temp.cel
37.77777777777778
>>> 
