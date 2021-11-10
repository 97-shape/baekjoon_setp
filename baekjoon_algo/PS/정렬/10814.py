import sys

info = []

for i in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().split()
    info.append((int(age), name))

info.sort(key=lambda info: info[0])

for x in info:
    print(x[0], x[1])