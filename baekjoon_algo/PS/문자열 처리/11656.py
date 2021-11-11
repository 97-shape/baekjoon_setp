import sys

s = sys.stdin.readline().rstrip()
S = []

for i in range(len(s)):
    S.append(s[i:])
S.sort()

for x in S:
    print(x)