import sys

n = int(sys.stdin.readline().rstrip())
info = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    info.append((int(age), str(name), i))

info.sort(key=lambda info: (info[0], info[2]))

for i in info:
    print(i[0], i[1])
