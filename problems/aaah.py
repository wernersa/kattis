import sys

lines = sys.stdin.readlines()
possible, requirement = [len(line) for line in lines]

if possible >= requirement:
    print("go")
else:
    print("no")
