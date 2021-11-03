import sys

s = list(map(str, sys.stdin.readline().rstrip()))

for i in range(0, len(s), 10):
    print("".join(s[i:i+10]))