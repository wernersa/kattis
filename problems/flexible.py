import sys

W, P = [int(k) for k in sys.stdin.readline().split(" ")]
partitions = [int(k) for k in sys.stdin.readline().split(" ")]

partitions = [0] + partitions + [W]

ans = set()

for i in range(len(partitions)):
    start = partitions[i]
    for j in range(i + 1, len(partitions)):
        end = partitions[j]
        ans.add(end - start)

ans = sorted(list(ans))

print(" ".join((str(k) for k in ans)))
