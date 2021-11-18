import sys
# RecursionError 해결방법 https://help.acmicpc.net/judge/rte/RecursionError
# Python 기본 최대 재귀 깊이보다 더 깊어질때 발생
sys.setrecursionlimit(100000)  # 최대 재귀 깊이 수정

def DFS(v):
    ch[v] = 1
    for i in range(1, n+1):
        if node[v][i] == 1 and ch[i] == 0:
            DFS(i)

n, m = map(int, sys.stdin.readline().split())
node = [[0] * (n+1) for _ in range(n+1)]

ch = [0] * (n+1)
cnt = 0

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    node[x][y] = 1
    node[y][x] = 1

for i in range(1, n+1):
    if ch[i] == 0:
        DFS(i)
        cnt += 1

print(cnt)