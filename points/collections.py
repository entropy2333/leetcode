# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x, p.y)

# Circle = namedtuple('Circle', ['x', 'y', 'r'])

# from collections import deque

# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# from collections import defaultdict

# dd = defaultdict(lambda: 'N/A')
# dd['key'] = 'abc'
# print(dd['key'], dd['value'])

# from collections import OrderedDict

# class LastUpdatedOrderedDict(OrderedDict):

#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity

#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)

# from collections import ChainMap
# import os, argparse

# # 构造缺省参数:
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }

# # 构造命令行参数:
# parser = argparse.ArgumentParser()
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# namespace = parser.parse_args()
# command_line_args = { k: v for k, v in vars(namespace).items() if v }

# # 组合成ChainMap:
# combined = ChainMap(command_line_args, os.environ, defaults)

# # 打印参数:
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])

# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)
  