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

