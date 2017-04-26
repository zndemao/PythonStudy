Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 集合
>>> num={}
>>> type(num)
<class 'dict'>
>>> num2={1,2,3,4,5}
>>> type(num2)
<class 'set'>
>>> # set
>>> #一堆数字没有体现映射关系，为集合
>>> num2={1,2,3,4,5,5,4,3,2,1}
>>> num2
{1, 2, 3, 4, 5}
>>> num2[2]#不支持
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    num2[2]#不支持
TypeError: 'set' object does not support indexing
>>> # 一种是直接把一堆元素用花括号括起来
>>> # 一种是使用set（）工厂方法
>>> # 创建集合的两种方法
>>> set1=set([1,2,3,4,5,5])#可以传进一个列表，元祖，字符串
>>> set1
{1, 2, 3, 4, 5}
>>> list1=[1,2,3,4,5,5,3]
>>> set2=set(list1)
>>> set2
{1, 2, 3, 4, 5}
>>> tem[=[]
    
SyntaxError: invalid syntax
>>> temp=[]
>>> for each in list1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5]
>>> list1=[1,4,6,7,8,2,3,4,5,5,3]
>>> set3=set(list1)
>>> set3
{1, 2, 3, 4, 5, 6, 7, 8}
>>> i in set3
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    i in set3
NameError: name 'i' is not defined
>>> 1 in set3
True
>>> 0 in set3
False
>>> set3.add(6)
>>> set3
{1, 2, 3, 4, 5, 6, 7, 8}
>>> set3.add(9)
>>> set3
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> set.remove(1)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    set.remove(1)
TypeError: descriptor 'remove' requires a 'set' object but received a 'int'
>>> set3.remove(1)
>>> set3
{2, 3, 4, 5, 6, 7, 8, 9}
>>> #不可改变的集合
>>> #集合不能被随意增加或者删除
>>> set4=frozenset(list1)
>>> set4
frozenset({1, 2, 3, 4, 5, 6, 7, 8})
>>> set4.add(0)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    set4.add(0)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
