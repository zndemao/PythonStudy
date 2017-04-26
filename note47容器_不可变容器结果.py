Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 定制容器
>>> # 协议是什么，与其他语言的接口相似
>>> # 不可变，定义__len__()  __getitem__()
>>> # 可变,定义__len__()  __getitem__()  __setitem__()  __delitem__()
>>> 
========== RESTART: E:/Users/zxl96/Documents/python/note48不可变容器.py ==========
>>> c1=CountList (1,3,5,6)
>>> c2=CountList(2,4,7)
>>> c1[1]
3
>>> c2[0]
2
>>> c1[1]+c2[1]
7
>>> c1.count
{0: 0, 1: 2, 2: 0, 3: 0}
>>> c2.count
{0: 1, 1: 1, 2: 0}
>>> 
