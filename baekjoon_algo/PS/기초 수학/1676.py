import sys

n = int(sys.stdin.readline())

f = 1
for i in range(2, n+1):
    f *= i

f = list(str(f).rstrip())
cnt = 0
for x in f[::-1]:
    if x == '0':
        cnt += 1
    else:
        print(cnt)
        break