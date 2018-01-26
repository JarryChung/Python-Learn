# -*- coding: utf-8 -*-

# list
classmates = ['Michael', 'Bob', 'Tracy']
length = len(classmates)

print(classmates, ":", length, classmates[2], "\n")

classmates.insert(0,"Jarry")
print(classmates, "\n")

classmates.pop()
print(classmates)

print("-------------------------------")

# tuple
project = ('Math','English','Chinese')
print(project, "\n")
# tuple
num = (1,)
print(num, "\n")
# number
number = (1)
print(number, "\n")

tup = ('Chung',classmates)
print(tup)

print("-------------------------------")

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'], "\n")
d['Adam'] = 67
print(d['Adam'], "\n")

# 存在对应的key-value则返回value
print(d.get('Bob'), "\n")
# 不存在则返回None
print(d.get('Jarry'), "\n")
# 测试key是否在字典中
print('Tracy' in d, "\n")
# 删除
d.pop('Bob')
print(d)

print("-------------------------------")

# set
# 要创建一个set，需要提供一个list作为输入集合
s1 = set([1, 2, 3])
print(s1, "\n")
s1.add(4)
s1.add(4)
print(s1, "\n")

# 集合操作
s2 = set([6,7,8])
print(s1 | s2)
print(s1 & s2)



