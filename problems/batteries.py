import sys
import math

MAX_N = 4711
tests = [0, 0]
i = 1
while len(tests) <= MAX_N:
    tests += [i] * i
    i += 1

for i in sys.stdin:
    if int(i) == 0:
        exit()
    else:
        print(tests[int(i)])