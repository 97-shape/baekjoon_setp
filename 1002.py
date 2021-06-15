import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rsplit())
    d = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
    sum_r = r1 + r2
    sub_r = abs(r2-r1)
    if d == 0:
        print(1)