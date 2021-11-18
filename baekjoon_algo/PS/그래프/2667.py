import sys
input = sys.stdin.readline

dx = [-1, 0 , 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and apt[xx][yy] == 1:
            apt[xx][yy] = 0
            cnt += 1
            DFS(xx,yy)

n = int(input())
apt = [list(map(int, input().rstrip())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            apt[i][j] = 0
            cnt = 1
            DFS(i, j)
            res.append(cnt)

print(len(res))
res.sort()
for r in res:
    print(r)