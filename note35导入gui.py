Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import easygui
>>> easygui.msgbox ('cat')
'OK'
>>> from easygui import *
>>> msgbox('cat')
'OK'
>>> import easygui as g
>>> g.msgbox ('cat')
'OK'
>>> # 推荐使用第三种，
