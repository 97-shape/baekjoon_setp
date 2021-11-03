import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    if i == n:
        print('*' * (2*n-1))
    elif i == 1:
        print(' ' * (n-i), end = '')
        print('*')
    else:
        print(' ' * (n-i), end = '')
        print('*', end = '')
        print(' ' * (2*i-3), end = '')
        print('*')