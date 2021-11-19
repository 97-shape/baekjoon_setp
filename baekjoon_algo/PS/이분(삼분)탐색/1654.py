import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
s, e = 1, max(lan)

while s<= e:
    m = (s+e) // 2
    lans = 0
    for l in lan:
        lans += l // m

    if lans >= n:
        s = m + 1
    else:
        e = m - 1
print(e)