import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

s, e = 1, arr[-1] - arr[0]
while s <= e:
    m = (s+e)//2
    last = arr[0]
    cnt = 1

    for i in range(1, n):
        if arr[i] >= last + m:  # arr[i]와 last의 거리가 m 보다 크거나 같은 경우
            cnt += 1
            last = arr[i]

    if cnt >= c:
        s = m + 1
        res = m
    else:
        e = m - 1

print(res)