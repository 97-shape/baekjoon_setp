import sys

n = int(sys.stdin.readline().rstrip())
point = []

for i in range(n):
    point.append(list(map(int, sys.stdin.readline().split())))

point.sort(key=lambda point: (point[1], point[0]))

for i in point:
    print(i[0], i[1])
