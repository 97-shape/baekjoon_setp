import sys

grade = []

for _ in range(int(sys.stdin.readline())):
    n, a, b, c = sys.stdin.readline().split()
    grade.append((n, int(a), int(b), int(c)))

grade.sort(key=lambda grade: (-grade[1], grade[2], -grade[3], grade[0]))

for g in grade:
    print(g[0])