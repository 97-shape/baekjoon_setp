import sys

num = [1, 2, 3]

def DFS(n, s):
    global cnt
    if s == n:
        cnt += 1
    if s > n:
        return
    else:
        for i in num:
            DFS(n, s+i)


t = int(sys.stdin.readline())

for _ in range(t):
    cnt = 0
    n = int(sys.stdin.readline())
    DFS(n, 0)
    print(cnt)