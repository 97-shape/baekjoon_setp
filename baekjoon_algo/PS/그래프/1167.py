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
    for i in range(1, len(a)-1, 2):  # -1 ������ ������ �Ÿ� ��
        tree[a[0]].append((a[i], a[i+1])) 

d, n = BFS(1)  # ��� 1 �������� ���� �� �Ÿ��� ���
d, n = BFS(n)  # �� ��忡�� ���� �� �Ÿ��� ������
print(d)
