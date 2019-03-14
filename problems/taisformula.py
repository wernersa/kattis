import sys

n = int(sys.stdin.readline())

times = list(range(n))
values = list(range(n))
mmols = list(range(n-1))

for i in range(n):
    times[i], values[i] = [float(x) for x in sys.stdin.readline().strip().split(" ")]
    if i > 0:
        mmols[i-1] = (values[i] + values[i-1]) / 2 * (times[i] - times[i-1]) / 1000

print(sum(mmols))