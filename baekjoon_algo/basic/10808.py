import sys

stack = [0] * 26

s = str(sys.stdin.readline().rstrip())

for i in s:
    stack[ord(i) - ord('a')] += 1

for j in stack:
    print(j, end=' ')