import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

s, e = 1, max(tree)

while s <= e:
    mid = (s+e) // 2
    cut = sum([l-mid if mid < l else 0 for l in tree]) #?
    if cut >= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)