from collections import deque

n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
idx = 0
result = []
while q:
    idx += 1
    if idx == k:
        result.append(str(q.popleft()))
        idx = 0
    else:
        q.append(q.popleft())

print("<", end="")
print(", ".join(result), end=">")