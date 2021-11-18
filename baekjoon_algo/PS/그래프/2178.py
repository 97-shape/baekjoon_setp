import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m and maze[xx][yy] == 1:
            maze[xx][yy] += maze[x][y]
            q.append((xx, yy))

print(maze[n-1][m-1])