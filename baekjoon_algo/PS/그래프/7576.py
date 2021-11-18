import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m and arr[xx][yy] == 0:
            arr[xx][yy] = arr[x][y] + 1
            q.append((xx, yy))

flag = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag = 0

res = -1
if flag:
    for i in range(n):
        for j in range(m):
            if arr[i][j] > res:
                res = arr[i][j] - 1
print(res)