number = ['asus zenfone', 'lumia 830', 'mote x+1']
for i in number:
    print(i)
mix = [1, 'moto x+1', 3.14159, [1, 2, 'lumia']]
print(mix)
empty = []
print(empty)
# 列表里可以放任何元素，列表里可以放列表。可以是空列表
number.append('iphone 8')  # append属于列表这个类的bif
print(number)
number.extend(['nexus 5x', 'lumia'])  # 扩展列表
print(number)
number.insert(1, 'cat')  # 插入一个数据，python的列表是从0开始
print(number)
number.insert(0, 'tom')
print(number)
