import sys

n = int(sys.stdin.readline())
k = n * 2 - 1

for i in range(1, k + 1):
    if i <= n:
        print(' ' * (n-i), end='')
        print('*' * i)
    elif i > n:
        print(' ' * (i-n), end='')
        print('*' * (k-i+1))