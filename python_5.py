# -*- coding: utf-8 -*-

from collections import Iterable

# 切片,list & tuple & 字符串
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
lis = list(range(100))

print(L[0:3])

print(lis[:10])
print(lis[-10:])

print(lis[:20:2])       # 前10个数，每两个取一个

print("JarryChung"[:5])
print("---------------------------------")

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print(key, value)

for ch in "ABC":
    print(ch)

print(isinstance("ABC", Iterable))      # string是否可迭代
print(isinstance(123,Iterable))         # 整型是否可迭代

for i, value in enumerate(["A", "B", "C"]):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def min_and_max(L):
    min_value = L[0]
    max_value = L[0]
    for v in L:
        if min_value > v:
            min_value = v
        if max_value < v:
            max_value = v
    return min_value, max_value

min_v, max_v = min_and_max([1,6,2,4,8,9,3,5])
print(min_v, max_v)

print("---------------------------------")

# 列表生成式
print(list(range(10,13)))
print([x*x for x in range(1,9) if x % 2 == 1])
print([m+n for m in "ABC" for n in "XYZ"])

List = ['Hello', 'World', 18, 'Apple', None]
L = [x.lower() for x in List if isinstance(x,str)]
print(L)

print("---------------------------------")

# 生成器
g = (x * x for x in range(1, 8))
print(next(g))