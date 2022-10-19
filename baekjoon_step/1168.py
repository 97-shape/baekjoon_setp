from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
result = []

cnt = 1
while q:
    if cnt == k:
        result.append(str(q.popleft()))
        cnt = 1
    q.append(q.popleft())
    cnt += 1

print("<" + ", ".join(result) + ">")