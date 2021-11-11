import sys

n, b = map(int, sys.stdin.readline().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ''

while n != 0:
    res += str(arr[int(n%b)])
    n //=b

print(res[::-1])