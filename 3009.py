import sys

dots = []
dot_4 = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    dots += x, y

for i in range(2):
    if dots[i] == dots[i+2]:
        dot_4.append(dots[i+4])
    elif dots[i+2] == dots[i+4]:
        dot_4.append(dots[i])
    else:
        dot_4.append(dots[i+2])

print(dot_4[0], dot_4[1])
