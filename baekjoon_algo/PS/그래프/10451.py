import sys
sys.setrecursionlimit(1000000)

def DFS(v):
    ch[v] = 1
    if ch[arr[v]] == 0:
        DFS(arr[v])

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ch = [0 for i in range(n+1)]
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    cnt = 0

    for i in range(1, n+1):
        if ch[i] == 0:
            DFS(i)
            cnt += 1
    print(cnt)