import sys

n = int(sys.stdin.readline())
d = [0] * (n+1)

if n < 3:
    print(2 * n - 1)
else:
    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2] * 2

    print(d[n] % 10007)