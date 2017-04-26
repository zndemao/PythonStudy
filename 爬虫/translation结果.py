Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========= RESTART: E:/Users/zxl96/Documents/python/爬虫/translation.py =========
                                                                                                                                              {"type":"EN2ZH_CN","errorCode":0,"elapsedTime":0,"translateResult":[[{"src":"i love your","tgt":"我爱你"}]],"smartResult":{"type":1,"entries":["","我是真心爱你的"]}}

>>> import json
>>> json.loads(html)
{'type': 'EN2ZH_CN', 'errorCode': 0, 'elapsedTime': 0, 'translateResult': [[{'src': 'i love your', 'tgt': '我爱你'}]], 'smartResult': {'type': 1, 'entries': ['', '我是真心爱你的']}}
>>> target=json.loads(html)
>>> type(target)
<class 'dict'>
>>> target['translateResult']
[[{'src': 'i love your', 'tgt': '我爱你'}]]
>>> target['translateResult'][0][0]
{'src': 'i love your', 'tgt': '我爱你'}
>>> target['translateResult'][0][0]['tgt']
'我爱你'
>>> 
========= RESTART: E:/Users/zxl96/Documents/python/爬虫/translation.py =========
请输入要翻译的内容:i love your
翻译结果:我爱你
>>> 
========= RESTART: E:/Users/zxl96/Documents/python/爬虫/translation.py =========
请输入要翻译的内容:love
翻译结果:爱
>>> 
