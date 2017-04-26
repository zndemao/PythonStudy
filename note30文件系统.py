Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 模块
>>> import random
>>> secret=random.randint (1,10)
>>> secret
8
>>> import os
>>> os.getcwd()
'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> #返回当前工作目录
>>> os.chdir ('F:\\')
>>> #改变工作目录
>>> os.getcwd()
'F:\\'
>>> os.chdir ('F:\\A')
>>> os.getcwd ()
'F:\\A'
>>> #列举指定目录中的文件名
>>> os.listdir()
['A']
>>> os.mkdir('B')
>>> #'创建单程层目录,如果该目录已经存在抛出异常'
>>> os.listdir()
['A', 'B']
>>> os.mkdir('B\\C')
>>> os.listdir()
['A', 'B']
>>> os.remove
<built-in function remove>
>>> os.remove('F:\\A')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    os.remove('F:\\A')
PermissionError: [WinError 5] 拒绝访问。: 'F:\\A'
>>> os.rmdir('F:\\A')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.rmdir('F:\\A')
PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'F:\\A'
>>> os.remove('F:\\A')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    os.remove('F:\\A')
PermissionError: [WinError 5] 拒绝访问。: 'F:\\A'
>>> os.rmdir('F:\\A')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    os.rmdir('F:\\A')
PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'F:\\A'
>>> os.system ('cmd')
-1073741510
>>> os.curdir
'.'
>>> os.listdir(os.curdir)
['A', 'B']
>>> os.sep
'\\'
>>> os.linesep
'\r\n'
>>> os.name
'nt'
>>> os.path
<module 'ntpath' from 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\ntpath.py'>
>>> os.path.basename('F:\\A')
'A'
>>> os.path.basename('F:\\A\\A')
'A'
>>> os.path.dirname('F:\\A\\A')
'F:\\A'
>>> os.path.join('A',"B","C")
'A\\B\\C'
>>> os.path.split ('F:\\A\\A\\test')
('F:\\A\\A', 'test')
>>> os.path.splitext ('F:\\A\\A\\test')
('F:\\A\\A\\test', '')
>>> os.path.splitext ('F:\\A\\A\\test.txt')
('F:\\A\\A\\test', '.txt')
>>> os.path.split ('F:\\A\\A\\test.txt')
('F:\\A\\A', 'test.txt')
>>> os.path.getsize ()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    os.path.getsize ()
TypeError: getsize() missing 1 required positional argument: 'filename'
>>> os.path.getatime('F:\\A\\A\\test.txt')
1491807976.455201
>>> os.path.getctime('F:\\A\\A\\test.txt')
1491807976.455201
>>> os.path.getmtime('F:\\A\\A\\test.txt')
1491807976.455201
>>> import time
>>> time.gmtime(os.path.getatime('F:\\A\\A\\test.txt'))
time.struct_time(tm_year=2017, tm_mon=4, tm_mday=10, tm_hour=7, tm_min=6, tm_sec=16, tm_wday=0, tm_yday=100, tm_isdst=0)
>>> time.localtime(os.path.getatime('F:\\A\\A\\test.txt'))
time.struct_time(tm_year=2017, tm_mon=4, tm_mday=10, tm_hour=15, tm_min=6, tm_sec=16, tm_wday=0, tm_yday=100, tm_isdst=0)
>>> os.path.ismount ('F:\\')
True
>>> 
