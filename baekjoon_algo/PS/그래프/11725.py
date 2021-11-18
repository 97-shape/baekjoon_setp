import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def DFS(v):
    global parents
    for t in tree[v]:
        # ���� ��尡 �������� ���� ���
        if parents[t] == 0:
            parents[t] = v
            DFS(t)

n = int(input())

tree = [[] for _ in range(n+1)]

parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

DFS(1)

for i in range(2, n+1):
    print(parents[i])