Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # \A == ^
>>> # \A == ^
>>> # \Z == $
>>> # 有区别，^$可以匹配换行之后
>>> import re
>>> re.findall(r'\bcat\b','cat.com!cat_com!(cat)')
['cat', 'cat']
>>> re.findall(r'\Bcat\B','cat.com!cat_com!(cat)')
[]
>>> re.findall(r'\d','123')
['1', '2', '3']
>>> re.search(r'\d','123')
<_sre.SRE_Match object; span=(0, 1), match='1'>
>>> # \w [a-zA-Z0-9]
>>> re.findall(r'\w','刚刚好（xue）')
['刚', '刚', '好', 'x', 'u', 'e']
>>> re.findall(r'\w','刚刚好 （xue_）')
['刚', '刚', '好', 'x', 'u', 'e', '_']
>>> re.findall(r'\W','刚刚好 （xue_）')
[' ', '（', '）']
>>> p=re.compile(r'[a-z]')
>>> type(p)
<class '_sre.SRE_Pattern'>
>>> p.search('cat')
<_sre.SRE_Match object; span=(0, 1), match='c'>
>>> p.findall ('cat')
['c', 'a', 't']
>>> 
