import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

def DFS(x, y):
    arr[x][y] = 0
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < h and 0 <= yy < w and arr[xx][yy] == 1:
            DFS(xx, yy)

while True:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                DFS(i, j)
    print(cnt)