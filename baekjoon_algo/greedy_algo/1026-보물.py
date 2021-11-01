import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

res = 0
while a:
    A = a.index(min(a))
    B = b.index(max(b))
    res += a.pop(A) * b.pop(B)

print(res)
