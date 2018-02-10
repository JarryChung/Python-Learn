# -*- coding: utf-8 -*-

# 高阶函数
func = abs
print(func(-9))


def abs_add(x, y, f):
    return f(x) + f(y)


print(abs_add(-5, 5, func))

