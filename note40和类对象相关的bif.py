Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 一个类被认为是其自身的子类
>>> # classinfo 可以是类对象组成的元祖，只要class与其中任何一个候选类的子类，则返回True
>>> class A:
	pass

>>> class B (A):
	pass

>>> issubclass(B,A)
True
>>> issubclass(B,B)
True
>>> issubclass(B,object)
True
>>> class C:
	pass

>>> issubclass(B ,C)
False
>>> # isinstance(object,classinfo)如果第一个参数不是对象，则永远返回False
>>> # 如果第二个参数不是类或者由类对象组成的元祖，会抛出一个TypeError异常
>>> b1=B()
>>> isinstance (b1,B)
True
>>> isinstance (b1,A)
True
>>> isinstance (b1,C)
False
>>> isinstance (b1,(A,B,C))
True
>>> # hasatter(object ,name) 测试对象是否有指定的属性
>>> class C:
	def __init__(self,x=0):
		self.x=x

		
>>> c1=C()
>>> hasattr (c1,'x')
True
>>> hasattr (c1,x)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    hasattr (c1,x)
NameError: name 'x' is not defined
>>> # getattr(ojbecrt,name,[,default])
>>> # 返回对象的属性值，
>>> getattr(c1,'x')
0
>>> getattr(c1,'y')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    getattr(c1,'y')
AttributeError: 'C' object has no attribute 'y'
>>> getattr(c1,'y','不存在')
'不存在'
>>> # setattr(ojbect,name,value)
>>> setattr(c1,'y','cat')
>>> getattr(c1,'y','不存在')
'cat'
>>> # delattr (ojbect ,name)
>>> delattr(c1,'y')
>>> delattr(c1,'y')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    delattr(c1,'y')
AttributeError: y
>>> # property(fget=None,fset=None,fde1=None,doc=None)
>>> class C:
	def __init__(self,size=10):
		self.size=size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size=value
	def delSize(self):
		del self.size
	x=property(getSize,setSize,delSize)

	
>>> c1=C()
>>> c1.getSize()
10
>>> c1.x
10
>>> c1.x=18
>>> c1.getSize ()
18
>>> del c1.x
>>> c1.size
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c1.size
AttributeError: 'C' object has no attribute 'size'
>>> 
