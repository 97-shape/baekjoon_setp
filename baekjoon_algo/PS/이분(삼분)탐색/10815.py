import sys
input = sys.stdin.readline

# 집합 사용

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print('1', end=' ')
    else:
        print('0', end=' ')

# 이분 탐색

def Binary(v):
    s, e = 0, n-1
    while s <= e:
        m = (s+e) // 2
        if a[m] == v:
            return 1
        elif a[m] > v:
            e = m - 1
        else:
            s = m + 1
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))
    
for i in b:
    res = Binary(i)
    if res:
        print(1, end=' ')
    else:
        print(0, end=' ')