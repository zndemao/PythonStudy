import urllib.request
import random

url = 'http://www.whatismyip.com.tw'

iplist=['221.179.236.245:8123','117.90.5.137:9000','117.90.5.219:9000','113.121.181.81:808']

proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
#opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
