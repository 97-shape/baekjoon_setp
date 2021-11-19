import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
    q = deque()
    q.append((v,0))
    ch = [0] * (n+1)
    ch[v] = 1
    res = [0, 0]

    while q:
        cur, dis = q.popleft()
        for t in node[cur]:
            next, dis2 = t
            if not ch[next]:
                ch[next] = 1
                q.append((next, dis+dis2))
                if res[1] < dis + dis2:
                    res = next, dis + dis2
    return res


n = int(input())
node = {i:[] for i in range(n+1)}  # n = 1 일 경우 BFS에서 node[0]의 값을 찾기 때문에 1 ~ n+1로 지정했을때 참조 오류가 발생했다

for _ in range(n-1):
    a, b, c = map(int, input().split())
    node[a].append((b, c))
    node[b].append((a, c))

Node, d = BFS(1)
Node, d = BFS(Node)
print(d)