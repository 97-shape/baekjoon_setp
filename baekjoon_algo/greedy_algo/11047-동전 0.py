import sys

n, k = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for _ in range(n)]

res = 0
for i in range(n-1, -1, -1):
	if k == 0:
		break
	if coin[i] > k:
		continue
	res += k // coin[i]
	k = k % coin[i]

print(res)