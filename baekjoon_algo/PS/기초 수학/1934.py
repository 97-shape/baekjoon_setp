import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    res = a*b
    while a > 0:
        a, b = b%a, a
    print(int(res / b))
