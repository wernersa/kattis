import sys
from collections import Counter

word = sys.stdin.readline().strip("\n")
counts = Counter(word)

if len(counts) <= 2:
    print(0)
else:

    for key, value in counts.most_common(2):
        counts.pop(key)

    print(sum(count for count in counts.values()))
