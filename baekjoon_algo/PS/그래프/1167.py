import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def BFS(l):
    ch = [-1] * (v+1)
    q = deque()
    q.append(l)
    ch[l] = 0
    res = [0, 0]

    while q:
        t = q.popleft()
        for s, e in tree[t]:
            if ch[s] == -1:
                ch[s] = ch[t] + e
                q.append(s)
                if res[0] < ch[s]:
                    res = ch[s], s
    return res

v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    a = list(map(int, input().split()))
    for i in range(1, len(a)-1, 2):  # -1 이전의 정점과 거리 값
        tree[a[0]].append((a[i], a[i+1])) 

d, n = BFS(1)  # 노드 1 기준으로 가장 먼 거리의 노드
d, n = BFS(n)  # 위 노드에서 가장 먼 거리의 노드까지
print(d)
