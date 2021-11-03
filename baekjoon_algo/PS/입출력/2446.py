import sys

n = int(sys.stdin.readline())
k = n * 2 - 1

for i in range(0, k):
    if i < n:
        print(' ' * i, end='')
        print('*' * (k- 2 * i))
    else:
        print(' ' * (k-i-1), end='')
        print('*' * (2 * i - k + 2))