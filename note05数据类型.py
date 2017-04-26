Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Pyton只用名字，没有数据类型
>>> #（数值类型）整形，浮点型，布尔类型，e记法
>>> #整形
>>> #已经包含长整形
>>> #e记法
>>> a=0.0000000000000000000000000000000001
>>> a
1e-34
>>> 1500000000000000000000000000000000000000000
1500000000000000000000000000000000000000000
>>> 1.5e22
1.5e+22
>>> 1.5E22
1.5e+22
>>> 15000
15000
>>> 1.4e4
14000.0
>>> 1.5e4
15000.0
>>> #布尔类型
>>> #True相当于1，False相当于0
>>> True+True
2
>>> True+False
1
>>> #转换
>>> a='520'
>>> int(a)
520
>>> string='string'
>>> int(string)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(string)
ValueError: invalid literal for int() with base 10: 'string'
>>> number=5.5
>>> int(number)
5
>>> number=5
>>> float(number)
5.0
>>> string='5.5'
>>> float(string)
5.5
>>> s='5'
>>> float(s)
5.0
>>> number=5
>>> str
<class 'str'>
>>> str(number)
'5'
>>> number=5.555
>>> str(number)
'5.555'
>>> #str是内置函数，不能当作变量名
>>> #获取数据类型
>>> type(number)
<class 'float'>
>>> type(string)
<class 'str'>
>>> isinstance(number)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    isinstance(number)
TypeError: isinstance expected 2 arguments, got 1
>>> isinstance(number,int)
False
>>> isinstance(number,float)
True
>>> isinstance(number,str)
False
>>> isinstance(string,int)
False
>>> isinstance(string,str)
True
>>> a=5
>>> isinstance(a,int)
True
>>> b=True
>>> type(b)
<class 'bool'>
>>> isinstance(b,bool)
True
>>> isinstance(b,str)
False
>>> isinstance(b,int)
True
>>> isinstance(b,bool)
True
>>> 
