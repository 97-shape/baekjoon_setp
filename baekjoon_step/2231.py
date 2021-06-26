import sys

m = int(sys.stdin.readline().rstrip())

n = 0

for i in range(1, m+1):
    list_i = list(map(int, str(i)))
    n = i + sum(list_i)
    if n == m:
        n = i
        break

if i == m:
    n = 0

print(n)
