n, m = map(int, input().split())

block = 0
if n == 1:
    block = 1
elif n == 2:
    block = min(4, (m-1)//2 + 1)
elif m < 7:
    block = min(4, m)
else:
    block = m - 2
print(block)