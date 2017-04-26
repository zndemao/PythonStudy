Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path
['', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
>>> # site-packages 存放模块的文件夹
>>> sys.path.append("E:\\Users\\zxl96\\Documents\\python\\note51模块_搜索路径和测试")
>>> sys.path
['', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32', 'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages', 'E:\\Users\\zxl96\\Documents\\python\\note51模块_搜索路径和测试']
>>> import TempConv
>>> import TempConv as tc
>>> tc.f2c(32)
0.0
>>> tc.f2c(99)
37.22222222222222
>>> # 包
>>> # 包 （package）
>>> 
