# -*- coding: utf-8 -*-

from functools import reduce


# 高阶函数
func = abs
print(func(-9))


def abs_add(x, f):
    return f(x) + f(x)


print(abs_add(-5, func))


def inc(x):
    return x+1


def add(v, u):
    return v + u


L = list(map(inc, [1, 2, 3]))
print(L)

LL = reduce(add, [1, 2, 3, 4, 5])
print(LL)


# reduce & map 综合使用，将字符串转化为数字
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


# filter
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# sorted排序
print(sorted([-9,-11,11,9,0]))      # 按数值大小
print(sorted([-9,-11,11,9,0], key=abs))     # 按绝对值大小
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))       # 转化为小写字母排序并且反序

