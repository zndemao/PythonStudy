temp = [1, 2, 3]
# append
temp.append(4)
# extend
temp.extend([5, 6])
# insert
temp.insert(0, 0)
print(temp)
print(temp[0])
print(temp[3])
# 调换位置
tempNumber = temp[0]
temp[0] = temp[3]
temp[3] = tempNumber
print(temp)
temp.remove(3)  # 不需要知道那个位置，只用提供值
print(temp)
# temp.remove('nu')#必须在里面
print("*********")
del temp[2]  # 他是个语句
print(temp)

# temp.pop()  # 弹栈，取出最后一个元素
print(temp.pop())
print("----")
i = temp.pop()
print(i)
j = temp.pop(1)
print(j)
# 列表切片(分片)
print('列表切片')
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number[1: 3])
print(number)
print(number[:3])
print(number[:])

# del temp
# print(temp)  # Process finished with exit code 1 处理完成退出代码1
l = [1, 2, 3]
# del l
# print(l)
