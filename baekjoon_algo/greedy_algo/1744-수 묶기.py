import sys

N = int(sys.stdin.readline().rstrip())
p = []
n = []  # 0을 포함한 마이너스 값

res = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 1:
        res += 1
    elif num > 0:
        p.append(num)
    elif num <= 0:
        n.append(num)

p.sort(reverse=True)
n.sort()

if len(p) % 2 == 0:
    for i in range(0, len(p), 2):
        res += p[i] * p[i+1]
else:
    for i in range(0, len(p)-1, 2):
        res += p[i] * p[i+1]
    res += p.pop()

if len(n) % 2 == 0:
    for i in range(0, len(n), 2):
        res += n[i] * n[i+1]
else:
    for i in range(0, len(n)-1, 2):
        res += n[i] * n[i+1]
    res += n.pop()

print(res)