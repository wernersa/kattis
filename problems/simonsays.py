import sys
out = [line[10:] for line in sys.stdin if line[:10] == "Simon says"]
print("".join(out), end="")