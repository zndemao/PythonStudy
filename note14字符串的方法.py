# 字符串 2和3不同
str1 = 'I love wei'
print(str1[:6])
print(str1[5])
print(str1[:6] + '插入' + str1[6:])
s = 'love'
print('首字母改为大写  capitalize()')
s.capitalize()
print(s)
print('把字符串的全部改为小写  casefold()')
s1 = 'I LOVE love'
s1 = s1.casefold()  # 生成新的字符串，原字符串保留
print(s1)
print('将字符串居中，并用空格至长度wodth的新字符串 center')
print(s.center(10))
print('返回出现次数   count()')
print(s.count('l'))
print('检查是不是指定的结束 endswith（）')
print(s.endswith('e'))
print('把字符串的\\t转换为空格'
      '如果不指定参数，默认的空格数是tabsize==8'
      '     expandtabs()')
s2 = '    l08   o'
print(s2.expandtabs())
print('返回索引值，找不到返回-1'
      '     find()')
print(s.find('o'))
ss = 'test'
ss.isalnum()
ss.isalpha()
ss.isdecimal()
ss.isdigit()
ss.islower()
ss.isnumeric()
ss.isspace()
ss.title()
ss.isupper()
ss.join()
ss.ljust()
ss.lower()
ss.lstrip()
ss.partition()
ss.replace()
ss.rfind()
ss.rindex()
ss.rjust()
ss.rpartition()
ss.rstrip()
ss.split()
ss.swapcase()
ss.title()
ss.translate()
ss.upper()
ss.zfill()
