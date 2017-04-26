Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> result=re.search(r' (\w+) (\w+)','i love cat.com')
>>> result
<_sre.SRE_Match object; span=(1, 10), match=' love cat'>
>>> result.group()
' love cat'
>>> result.group(1)
'love'
>>> result.group(2)
'cat'
>>> result.start()
1
>>> result.end()
10
>>> result.span()
(1, 10)
>>> 
