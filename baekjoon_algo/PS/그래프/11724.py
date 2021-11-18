import sys
# RecursionError �ذ��� https://help.acmicpc.net/judge/rte/RecursionError
# Python �⺻ �ִ� ��� ���̺��� �� ������� �߻�
sys.setrecursionlimit(100000)  # �ִ� ��� ���� ����

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