import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
o = list(map(int, sys.stdin.readline().split()))

t = 0
res = []

for i in range(m):
    t += o[i] * (a ** (m-i-1))

while t != 0:
        res.append(str(t%b))
        t //= b

print(' '.join(res[::-1]))