# -*- encoding: utf-8 -*-

import re

s = r'Jarry\-Chung'                 # 使用Python的r前缀，就不用考虑转义的问题
print(s)

r = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(r)

print(re.split(r'\s+', 'a b   c'))

print(re.split(r'[\s\,]+', 'a,b, c  d'))

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))     # 用正则表达式来把不规范的输入转化成正确的数组

print("--------------------------------")

re_c = re.compile(r'^\d{3}\-\d{3,8}$')
print(re_c.match('010-12345').group())

re_s = re.compile(r'\s+')
print(re_s.split('a b   c'))

