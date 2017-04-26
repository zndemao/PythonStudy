import urllib.request as ur
import urllib.parse
import json

content = input('请输入要翻译的内容:')

# 链接
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.google.com.hk/'
# 字典
data = {}
data['type'] = 'AUTO'''
#data['i'] = 'i love your'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.8'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_ENTER'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')

response = ur.urlopen(url, data)
html = response.read().decode('utf-8')

target = json.loads(html)
print('翻译结果:%s' % (target['translateResult'][0][0]['tgt']))
