list1 = [1, 2, 3]
list2 = [2, 3, 4]
# 比较操作符
# 逻辑操作符
# 连接操作符
# 重复操作符
# 成员关系操作符
list3 = [123]
list4 = [234]
print(list3 > list4)
print(list1 > list2)  # 多个元素比较，只比较第一个
print(list1 < list2 and list3 < list4)
print(list1 + list2)  # 可以进行连接，但要求都为列表
print(list1 * 3)
list2 *= 4
print(list2)
print(1 in list1)
print(4 in list1)
print(1 not in list1)
print(4 not in list1)
print('-------')
list5 = [['1', 2], 3, '4']
print(2 in list5)
print(2 in list5[0])  # 人为引入
# 访问二维列表
print(list5[0][1])
print(dir(list))
print('============')
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(list2.count(2))  # 统计次数
print(list1.index(1))  # 返回第一次出现的位置
print(list2.index(2))
print(list2.index(2, 3, 7))  # 设置范围
# 整个列表原地翻转
print('整个列表原地翻转')
list1.reverse()
print(list1)
# 对整个列表进行排序
print('对整个列表进行排序')
list2.sort()
print(list2)  # 从小到大排列
list2.sort(reverse=True)  # 从小到大，再进行翻转
print(list2)
print('````````````````````')
list6 = list2[:]
print(list6)
list7 = list1
print(list7)
print('指针问题')
list1.reverse()
print(list7)
print(list1)

