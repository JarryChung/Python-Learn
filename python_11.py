# -*- coding: utf-8 -*-

from io import StringIO, BytesIO
import os

f = open('python_1.py', 'r')            # 以读方式打开文件python_1.py
print(f.read())
f.close()
print("--------------------------------")

try:
    f = open('python_1.py', 'r')        # 以读方式打开文件python_1.py
    print(f.read())
finally:
    if f:
        f.close()
print("--------------------------------")

with open('python_1.py', 'r') as f:     # 以读方式打开文件python_1.py，并自动关闭文件
    print(f.read())
print("--------------------------------")

with open('python_1.py', 'r') as f:     # 以按行读方式打开文件python_1.py，并自动关闭文件
    for line in f.readlines():
        print(line)
print("--------------------------------")

f = open('python_1.py', 'r', encoding='utf-8', errors='ignore')      # 传入encoding参数确认使用何种编码,errors参数表示如何处理编码错误
f.close()
print("--------------------------------------------------------------")


f = StringIO('Hello!\tHi!\tGoodbye!')
print(f.read())
ff = BytesIO()
ff.write('中文'.encode('utf-8'))           # f.write('中文'.encode('utf-8'))
print(ff.getvalue())
print("--------------------------------------------------------------")

print(os.uname())
print(os.environ)

# 查看、创建和删除目录
# 查看当前目录的绝对路径:
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/home/jarrychung', 'testdir')     # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 然后创建一个目录:
os.mkdir('/home/jarrychung/testdir')
# 删掉一个目录:
os.rmdir('/home/jarrychung/testdir')


