Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Python 只有名字，没有变量
>>> i=7
>>> i
7
>>> type(i)
<class 'int'>
>>> j=8
>>> k=i+j
>>> k
15
>>> 5+8
13
>>> '5'+'8'
'58'
>>> #转义符号
>>> 'Let\'s go!'
"Let's go!"
>>> print('C:\\now')
C:\now
>>> string=r'C;\now'#原始字符串
>>> string
'C;\\now'
>>> string=r'C:\now'#原始字符串
>>> string
'C:\\now'
>>> print(string)
C:\now
>>> strings='''雨渐渐停了，
你在哪呢，
谁哼着歌，
谁还寂寞。'''
>>> strings
'雨渐渐停了，\n你在哪呢，\n谁哼着歌，\n谁还寂寞。'
>>> print(strings)
雨渐渐停了，
你在哪呢，
谁哼着歌，
谁还寂寞。
>>> buqi='''雨被带走了，
你在哪呢.'''
>>> print(buqi)
雨被带走了，
你在哪呢.
>>> 
