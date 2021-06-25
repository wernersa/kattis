import sys

while True:
    n, m = [int(x) for x in sys.stdin.readline().split()]

    if n==0 and m==0:
        break

    catalog = set(int(sys.stdin.readline().strip()) for line in range(n))

    duplicates = 0
    for line in range(m):
        duplicates += int(sys.stdin.readline().strip()) in catalog

    print(duplicates)