import sys

def convert(x, y):
    global a
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]

n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            convert(i, j)
            cnt += 1

flag = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            flag = 1
            break

if flag:
    print(-1)
else:
    print(cnt)