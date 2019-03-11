import sys
W = [int(k) for k in sys.stdin.readlines()]
res = set()

for num in W:
    mod = num % 42
    res.add(mod)

print(len(res))