import sys
import heapq as h

n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]

h.heapify(cards)  # 리스트를 heap으로 변환

res = 0
while len(cards) != 1:
    a = h.heappop(cards)
    b = h.heappop(cards)
    res += a + b
    h.heappush(cards, a+b)

print(res)