import sys

n = int(sys.stdin.readline())
k = n * 2 - 1

for i in range(1, k + 1):
    if i <= n:
        print('*' * i, end='')
        print(' ' * 2 * (n-i), end='')
        print('*' * i)
    elif i > n:
        print('*' * (k-i+1), end='')
        print(' ' * 2 * (i-n), end='')
        print('*' * (k-i+1))