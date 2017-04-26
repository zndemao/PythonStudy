Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.search(r'cat|tom','cat')
<_sre.SRE_Match object; span=(0, 3), match='cat'>
>>> re.search(r'cat|tom','tom')
<_sre.SRE_Match object; span=(0, 3), match='tom'>
>>> re.search(r'^tom','tom')
<_sre.SRE_Match object; span=(0, 3), match='tom'>
>>> re.search(r'^tom','cat tom')
>>> re.search(r'tom$','tom cat')
>>> re.search(r'tom$','cat tom')
<_sre.SRE_Match object; span=(4, 7), match='tom'>
>>> re.search(r'(cat)\1','cat tom')
>>> re.search(r'(cat)\1','catcat')
<_sre.SRE_Match object; span=(0, 6), match='catcat'>
>>> # r'(cat)\1' == r'catcat'
>>> re.search(r'(cat)\060','catcat0')
<_sre.SRE_Match object; span=(3, 7), match='cat0'>
>>> re.search(r'(cat)\141','catcat')
>>> re.search(r'(cat)\141','catcata')
<_sre.SRE_Match object; span=(3, 7), match='cata'>
>>> re.search(r'.','catcata')
<_sre.SRE_Match object; span=(0, 1), match='c'>
>>> re.search(r'\.','catc.ata')
<_sre.SRE_Match object; span=(4, 5), match='.'>
>>> re.search(r'[.]','cat.tom')
<_sre.SRE_Match object; span=(3, 4), match='.'>
>>> re.findall (r'[a-z]','cat.tom')
['c', 'a', 't', 't', 'o', 'm']
>>> re.findall (r'[\]','cat.tom')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    re.findall (r'[\]','cat.tom')
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\re.py", line 222, in findall
    return _compile(pattern, flags).findall(string)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 856, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, False)
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 415, in _parse_sub
    itemsappend(_parse(source, state, verbose))
  File "E:\Users\zxl96\AppData\Local\Programs\Python\Python36-32\lib\sre_parse.py", line 522, in _parse
    source.tell() - here)
sre_constants.error: unterminated character set at position 0
>>> re.findall (r'[\n]','cat.tom\n')
['\n']
>>> re.findall (r'[^a-z]','cat.tom\n')
['.', '\n']
>>> # 取反 a-z之外的
>>> re.search(r'cat{3}','catcatcattt')
<_sre.SRE_Match object; span=(6, 11), match='cattt'>
>>> re.search(r'(cat){3}','catcatcattt')
<_sre.SRE_Match object; span=(0, 9), match='catcatcat'>
>>> re.search(r'(cat){1,5}','catcatcattt')
<_sre.SRE_Match object; span=(0, 9), match='catcatcat'>
>>> # 正则表达式不能随意加空格
>>> # * 零次或多次
>>> # + 一次或多次
>>> # ? 零次或一次
>>> s='<html><title>tom.cat</title></html>'
>>> re.search(r'<.+>',s)
<_sre.SRE_Match object; span=(0, 35), match='<html><title>tom.cat</title></html>'>
>>> re.search(r'<.+?>',s)
<_sre.SRE_Match object; span=(0, 6), match='<html>'>
>>> 
