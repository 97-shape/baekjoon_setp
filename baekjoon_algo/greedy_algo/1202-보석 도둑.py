import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

j = []
c = []

res = 0

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(j, (m, v))

for _ in range(k):
    c.append(int(sys.stdin.readline()))
c.sort()

temp = []
for b in c:
    while j and b >= j[0][0]:
        heapq.heappush(temp, -j[0][1])
        heapq.heappop(j)

    if temp:
        res -= heapq.heappop(temp)
    elif not j:
        break

print(res)