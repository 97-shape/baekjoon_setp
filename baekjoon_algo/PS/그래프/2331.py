import sys

def DFS(v):
    if v in d:
        print(d.index(v))
        return
    else:
        d.append(v)
        temp = 0
        for x in str(v):
            temp += int(x) ** p
        DFS(temp)

a, p = map(int, sys.stdin.readline().split())
d = []

DFS(a)