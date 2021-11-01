import sys

n = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

min_cost = cost[0]
res = 0
for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    res += min_cost * road[i]

print(res)