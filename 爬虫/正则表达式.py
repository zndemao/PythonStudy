Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> re.search(r'cat','tom cat')
<_sre.SRE_Match object; span=(4, 7), match='cat'>
>>> 'tom cat'.find('cat')
4
>>> re.search(r'.','tom cat')
<_sre.SRE_Match object; span=(0, 1), match='t'>
>>> re.search(r'cat.','tom cat.')
<_sre.SRE_Match object; span=(4, 8), match='cat.'>
>>> re.search(r'Fish.','I love FishC.com!')
<_sre.SRE_Match object; span=(7, 12), match='FishC'>
>>> re.search(r'\.','tom cat .')
<_sre.SRE_Match object; span=(8, 9), match='.'>
>>> # 元字符
>>> re.search(r'\d','tom 123 cat .')
<_sre.SRE_Match object; span=(4, 5), match='1'>
>>> re.search(r'\d\d\d','tom 123 cat .')
<_sre.SRE_Match object; span=(4, 7), match='123'>
>>> re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.101.122')
<_sre.SRE_Match object; span=(0, 15), match='192.168.101.122'>
>>> re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.1.1')
>>> # 字符类 []
>>> re.search(r'[aeiou]','tom cat')
<_sre.SRE_Match object; span=(1, 2), match='o'>
>>> re.search(r'[aeiouAEIOU]','O tom cat')
<_sre.SRE_Match object; span=(0, 1), match='O'>
>>> re.search(r'[a-z]','tom cat')
<_sre.SRE_Match object; span=(0, 1), match='t'>
>>> re.search(r'[1-9]','tom 123 cat')
<_sre.SRE_Match object; span=(4, 5), match='1'>
>>> re.search(r'[12-9]','tom 123 cat')
<_sre.SRE_Match object; span=(4, 5), match='1'>
>>> re.search(r'[2-9]','tom 123 cat')
<_sre.SRE_Match object; span=(5, 6), match='2'>
>>> re.search(r'ab{3}','abbbc')
<_sre.SRE_Match object; span=(0, 4), match='abbb'>
>>> re.search(r'ab{3}c','abbbc')
<_sre.SRE_Match object; span=(0, 5), match='abbbc'>
>>> re.search(r'ab{3}c','abbbbc')
>>> re.search(r'ab{3,10}c','abbbbc')
<_sre.SRE_Match object; span=(0, 6), match='abbbbc'>
>>> re.search(r'[01]\d\d | 2[2-4]\d | 25[0-5]','197')
>>> re.search(r'[01]\d\d|2[2-4]\d|25[0-5]','197')
<_sre.SRE_Match object; span=(0, 3), match='197'>
>>> re.search(r'[01]\d\d|2[2-4]\d|25[0-5]','1')
>>> re.search(r'[01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d','1')
<_sre.SRE_Match object; span=(0, 1), match='1'>
>>> re.search(r'[01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d','134')
<_sre.SRE_Match object; span=(0, 3), match='134'>
>>> re.search(r'[01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d','13')
<_sre.SRE_Match object; span=(0, 2), match='13'>
>>> re.search(r'(([01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d)\.){3}([01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d)','192.168.1.1')
<_sre.SRE_Match object; span=(0, 11), match='192.168.1.1'>
>>> ip=re.search(r'(([01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d)\.){3}([01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d)','192.168.1.1')
>>> ip
<_sre.SRE_Match object; span=(0, 11), match='192.168.1.1'>
>>> ip=re.search(r'(([01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d)\.){3}([01]\d\d|2[2-4]\d|25[0-5]|\d\d|\d)','192.168.1.1')
>>> ip
<_sre.SRE_Match object; span=(0, 11), match='192.168.1.1'>
>>> ip = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]\d{0,1}\d{0,1}|2[0-4]\d|25[0-5])', '192.168.0.1')
>>> ip
<_sre.SRE_Match object; span=(0, 11), match='192.168.0.1'>
>>> re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]\d{0,1}\d{0,1}|2[0-4]\d|25[0-5])', '192.168.0.1')
<_sre.SRE_Match object; span=(0, 11), match='192.168.0.1'>
>>> 
