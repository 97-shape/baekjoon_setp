import sys
sys.setrecursionlimit(1000000)

def DFS(v):
    global res
    ch[v] = 1
    cycle.append(v)
    if ch[arr[v]]:
        if arr[v] in cycle:  # 마지막 학생이 함께하고 싶은 학생이 있다면
            res += cycle[cycle.index(arr[v]):]  # 마지막 학생이 선택한 학생부터 한 팀
            return
    else:
        DFS(arr[v])

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ch = [0 for _ in range(n+1)]
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    res = []
    for i in range(1, n+1):
        if ch[i] == 0:
            cycle = []
            DFS(i)

    print(n - len(res))
