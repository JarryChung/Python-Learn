# -*- coding: utf-8 -*-

import math

# 调用系统函数
a = abs
print(a(-9), "\n")
print(hex(666666), "\n")


# 定义函数
def my_abs(x):
    if x > 0:
        return x
    if x < 0:
        return -x
    if x == 0:
        pass  # 占位符，pass语句什么都不做


print(my_abs(-6))


def move(x, y, step=100, angle=0):  # 含有默认参数，需从右到左含有。
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  # 返回多个值


x, y = move(100, 100, 60, math.pi / 6)  # 返回两个值
print(x, y)
r = move(100, 100, 60, math.pi / 6)  # 事实上，返回的是一个“值”tuple
print(r)


def calc(*numbers):  # 可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
nums = [1, 2, 3]
print(calc(*nums))


def person(name, age, **kw):  # 关键字参数
    print('name:', name, 'age:', age, 'other:', kw)


print(person('Adam', 45, gender='M', job='Engineer'))
print(person('Michael', 30))


def persons(name, age, *, city, job):  # 命名关键字参数
    print(name, age, city, job)


print(persons("Jarry", 20, city="Guangzhou", job="Net"))        # 末尾有None


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2, 3, 'a', 'b', x=99)     # 末尾有None
f2(1, 2, d=99, ext=None)        # 末尾有None


def fact(n):  # 递归函数(阶乘)
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 尾递归优化(阶乘)
def fact_w(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_w(5))