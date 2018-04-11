# -*- encoding: utf-8 -*-

from datetime import datetime
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


now = datetime.now()            # 获取当前日期和时间
print(now)

dt = datetime(1995, 11, 21, 11, 21, 55)     # 获取指定日期和时间
print(dt)

ts = dt.timestamp()             # datetime转换为timestamp
print(ts)

print(datetime.fromtimestamp(ts))           # timestamp转换为datetime
print(datetime.utcfromtimestamp(ts))        # timestamp转换为datetime(UTC时间)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')      # str转换为datetime
print(cday)

print(dt.strftime('%a, %b %d %H:%M'))    # datetime转换为str

print("------------------------------------")

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, ',', p.y)

q = deque(['a', 'b', 'c', 'd'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['k1'] = 123
print(dd['k1'])
print(dd['k2'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

count = Counter()
for c in 'afadasaf':
    count[c] = count[c] + 1
print(count)

print("------------------------------------")

