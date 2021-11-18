import sys
from collections import deque

def DFS(l, v):
    print(v, end = ' ')
    ch[v] = 1
    for i in range(1, n+1):
        if node[v][i] == 1 and ch[i] == 0:
            ch[i] = 1
            DFS(l+1, i)

n, m, v = map(int, sys.stdin.readline().split())
node = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    node[x][y] = 1
    node[y][x] = 1

DFS(1, v)
print()

#BFS
q = deque([v])
ch = [0] * (n+1)
ch[v] = 1
print(v, end=' ')
while q:
    x = q.popleft()
    for i in range(1, n+1):
        if node[x][i] == 1 and ch[i] == 0:
            ch[i] = 1
            print(i, end=' ')
            q.append(i)