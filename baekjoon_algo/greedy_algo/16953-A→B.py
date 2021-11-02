import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

Q = deque([(a, 1)])

while Q:
    n, i = Q.popleft()
    x = n * 2
    y = n * 10 + 1
    if not x > b:
        Q.append((x, i+1))
    if not y > b:
        Q.append((y, i+1))
    if x == b or y == b:
        flag = 0
        print(i+1)
        break
else:
    print(-1)