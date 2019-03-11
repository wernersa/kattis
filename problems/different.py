import sys
from functools import reduce

for i in sys.stdin:
    line = i.split()
    res = reduce(lambda x, y: int(x)-int(y), line)
    print(abs(res))
