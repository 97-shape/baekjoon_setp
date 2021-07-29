import sys

stack = [-1] * 26

s = str(sys.stdin.readline().rstrip())
k = 1
for i in s:
    if stack[ord(i) - ord('a')] == -1:
        stack[ord(i) - ord('a')] += k
    k += 1

for j in stack:
    print(j, end=' ')