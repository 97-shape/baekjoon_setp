import sys

n, k = map(int, sys.stdin.readline().split())

circle = [i+1 for i in range(n)]
result = []
pop = 0

for i in range(n):
    pop += k-1
    if pop >= len(circle):
        pop %= len(circle)
    result.append(str(circle.pop(pop)))

print('<', ', '.join(result), '>', sep='')
