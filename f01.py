#关于fluent python的笔记
#列表推导
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

for tshirt in ('%s %s' % (c, s) for c in colors for s in range(10)):
    print(tshirt)

#元组经常被作为 不可变列表 的代表. 经常只要数字索引获取元素, 但其实它还可以给元素命名
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
City(
    name='Tokyo',
    country='JP',
    population=36.933,
    coordinates=(35.689722, 139.691667))
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])
