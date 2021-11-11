import sys

n, k = map(int, sys.stdin.readline().split())
p = [i for i in range(1, n+1)]
res = []

pop = 0
while p:
    pop += k-1
    if pop >= len(p):
        pop %= len(p)
    res.append(str(p.pop(pop)))

print('<', ', '.join(res), '>', sep='')