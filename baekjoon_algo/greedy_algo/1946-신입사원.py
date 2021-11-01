import sys

def select(arr, n):
    cnt = 1
    h = arr[0][1]
    for i in range(1, n):
        if arr[i][1] < h:
            cnt += 1
            h = arr[i][1]
    return cnt

t = int(sys.stdin.readline())

res = []

for i in range(t):
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[0])
    res.append(select(arr, n))

for x in res:
    print(x)