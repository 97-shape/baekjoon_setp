import sys

i = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0 and p == 0 and v == 0:
        break
    a = v // p
    b = v % p
    if b > l:
        b = l
    print("Case {0}: {1}".format(i, l * a + b))
    i += 1