Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pickle
>>> my_list=[123,3.14,'cat',['tom']]
>>> import os
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'E:\\Users\\zxl96\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.chdir ('F:\\A')
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'F:\\A'
>>> pickle_file=open('my_list.pk1','wb')
>>> pickle .dump (my_list,pickle_file)
>>> pickle_file .close()
>>> pickle_file=open('my_list.pk1','rb')
>>> my-List2=pickle.load (pickle_file)
SyntaxError: can't assign to operator
>>> my_list2=pickle.load (pickle_file)
>>> print (my_list2 )
[123, 3.14, 'cat', ['tom']]
>>> top_list_all = {
    0: ['云音乐新歌榜', '/discover/toplist?id=3779629'],
    1: ['云音乐热歌榜', '/discover/toplist?id=3778678'],
    2: ['网易原创歌曲榜', '/discover/toplist?id=2884035'],
    3: ['云音乐飙升榜', '/discover/toplist?id=19723756'],
    4: ['云音乐电音榜', '/discover/toplist?id=10520166'],
    5: ['UK排行榜周榜', '/discover/toplist?id=180106'],
    6: ['美国Billboard周榜', '/discover/toplist?id=60198'],
    7: ['KTV嗨榜', '/discover/toplist?id=21845217'],
    8: ['iTunes榜', '/discover/toplist?id=11641012'],
    9: ['Hit FM Top榜', '/discover/toplist?id=120001'],
    10: ['日本Oricon周榜', '/discover/toplist?id=60131'],
    11: ['韩国Melon排行榜周榜', '/discover/toplist?id=3733003'],
    12: ['韩国Mnet排行榜周榜', '/discover/toplist?id=60255'],
    13: ['韩国Melon原声周榜', '/discover/toplist?id=46772709'],
    14: ['中国TOP排行榜(港台榜)', '/discover/toplist?id=112504'],
    15: ['中国TOP排行榜(内地榜)', '/discover/toplist?id=64016'],
    16: ['香港电台中文歌曲龙虎榜', '/discover/toplist?id=10169002'],
    17: ['华语金曲榜', '/discover/toplist?id=4395559'],
    18: ['中国嘻哈榜', '/discover/toplist?id=1899724'],
    19: ['法国 NRJ EuroHot 30周榜', '/discover/toplist?id=27135204'],
    20: ['台湾Hito排行榜', '/discover/toplist?id=112463'],
    21: ['Beatport全球电子舞曲榜', '/discover/toplist?id=3812895']
    top_list-all
    
SyntaxError: invalid syntax
>>> top_list_all = {
    0: ['云音乐新歌榜', '/discover/toplist?id=3779629'],
    1: ['云音乐热歌榜', '/discover/toplist?id=3778678'],
    2: ['网易原创歌曲榜', '/discover/toplist?id=2884035'],
    3: ['云音乐飙升榜', '/discover/toplist?id=19723756'],
    4: ['云音乐电音榜', '/discover/toplist?id=10520166'],
    5: ['UK排行榜周榜', '/discover/toplist?id=180106'],
    6: ['美国Billboard周榜', '/discover/toplist?id=60198'],
    7: ['KTV嗨榜', '/discover/toplist?id=21845217'],
    8: ['iTunes榜', '/discover/toplist?id=11641012'],
    9: ['Hit FM Top榜', '/discover/toplist?id=120001'],
    10: ['日本Oricon周榜', '/discover/toplist?id=60131'],
    11: ['韩国Melon排行榜周榜', '/discover/toplist?id=3733003'],
    12: ['韩国Mnet排行榜周榜', '/discover/toplist?id=60255'],
    13: ['韩国Melon原声周榜', '/discover/toplist?id=46772709'],
    14: ['中国TOP排行榜(港台榜)', '/discover/toplist?id=112504'],
    15: ['中国TOP排行榜(内地榜)', '/discover/toplist?id=64016'],
    16: ['香港电台中文歌曲龙虎榜', '/discover/toplist?id=10169002'],
    17: ['华语金曲榜', '/discover/toplist?id=4395559'],
    18: ['中国嘻哈榜', '/discover/toplist?id=1899724'],
    19: ['法国 NRJ EuroHot 30周榜', '/discover/toplist?id=27135204'],
    20: ['台湾Hito排行榜', '/discover/toplist?id=112463'],
    21: ['Beatport全球电子舞曲榜', '/discover/toplist?id=3812895']}
>>> top_list_all
{0: ['云音乐新歌榜', '/discover/toplist?id=3779629'], 1: ['云音乐热歌榜', '/discover/toplist?id=3778678'], 2: ['网易原创歌曲榜', '/discover/toplist?id=2884035'], 3: ['云音乐飙升榜', '/discover/toplist?id=19723756'], 4: ['云音乐电音榜', '/discover/toplist?id=10520166'], 5: ['UK排行榜周榜', '/discover/toplist?id=180106'], 6: ['美国Billboard周榜', '/discover/toplist?id=60198'], 7: ['KTV嗨榜', '/discover/toplist?id=21845217'], 8: ['iTunes榜', '/discover/toplist?id=11641012'], 9: ['Hit FM Top榜', '/discover/toplist?id=120001'], 10: ['日本Oricon周榜', '/discover/toplist?id=60131'], 11: ['韩国Melon排行榜周榜', '/discover/toplist?id=3733003'], 12: ['韩国Mnet排行榜周榜', '/discover/toplist?id=60255'], 13: ['韩国Melon原声周榜', '/discover/toplist?id=46772709'], 14: ['中国TOP排行榜(港台榜)', '/discover/toplist?id=112504'], 15: ['中国TOP排行榜(内地榜)', '/discover/toplist?id=64016'], 16: ['香港电台中文歌曲龙虎榜', '/discover/toplist?id=10169002'], 17: ['华语金曲榜', '/discover/toplist?id=4395559'], 18: ['中国嘻哈榜', '/discover/toplist?id=1899724'], 19: ['法国 NRJ EuroHot 30周榜', '/discover/toplist?id=27135204'], 20: ['台湾Hito排行榜', '/discover/toplist?id=112463'], 21: ['Beatport全球电子舞曲榜', '/discover/toplist?id=3812895']}
>>> pickle_file=open('city_data.pkl','wb')
>>> pickle .dump
<built-in function dump>
>>> pickle .dump(top_list_all,pickle_file )
>>> pickle_file .close
<built-in method close of _io.BufferedWriter object at 0x03AB7B58>
>>> pickle_file .close（）
SyntaxError: invalid character in identifier
>>> pickle_file .close()
>>> 
