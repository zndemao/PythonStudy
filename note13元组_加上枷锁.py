# 限制列表  元组
# 定义后 无法改变
# 使用时很相似
#
# Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
# Type "copyright", "credits" or "license()" for more information.
# >>> # 限制列表  元组
# # 定义后 无法改变
# # 使用时很相似
# >>> tuple1=(1,2,3,4,5,6,7)
# >>> tuple1[1]
# 2
# >>> list1=[1,2,3,4,5,6,7]
# >>> list1[1]
# 2
# >>> tuple1[:5]
# (1, 2, 3, 4, 5)
# >>> list1[:5]
# [1, 2, 3, 4, 5]
# >>> teple2=tuple1[:]
# >>> teple2
# (1, 2, 3, 4, 5, 6, 7)
# >>> teple1[1]=3
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     teple1[1]=3
# NameError: name 'teple1' is not defined
# >>> #定义元组的是 ,
# >>> temp=(1)
# >>> type(temp)
# <class 'int'>
# >>> temp1=2,4,5
# >>> type(temp1)
# <class 'tuple'>
# >>> temp2=[]
# >>> type(list2)
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     type(list2)
# NameError: name 'list2' is not defined
# >>> type(temp2)
# <class 'list'>
# >>> temp3=(1,)
# >>> type(temp3)
# <class 'tuple'>
# >>> temp4=1,
# >>> type(temp4)
# <class 'tuple'>
# >>> 8*(8)
# 64
# >>> 8*(8,)
# (8, 8, 8, 8, 8, 8, 8, 8)
# >>> #更新 OR 删除
# >>> tuple1=temp1[:2]+0+[2:]
# SyntaxError: invalid syntax
# >>> tuple1=temp1[:2]+0,+[2:]
# SyntaxError: invalid syntax
# >>> tuple1=temp1[:2]+(0,)+[2:]
# SyntaxError: invalid syntax
# >>> tuple1=tuple1[:2]+(0,)+[2:]
# SyntaxError: invalid syntax
# >>> tuple1=tuple1[:2]+(0,)+[2:]
# SyntaxError: invalid syntax
# >>> tuple1=tuple1[:2]+(0,)+tuple1[2:]
# >>> tuple1
# (1, 2, 0, 3, 4, 5, 6, 7)
# >>> del tuple1
# >>> tuple1
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     tuple1
# NameError: name 'tuple1' is not defined
# >>> #可以使用的操作符有
# >>> #拼接
# >>> #重复
# >>> #关系
# >>> #逻辑
# >>> #成员
# >>>
