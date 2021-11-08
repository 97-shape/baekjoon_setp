import sys

dp = [1] * (4)
dp.extend([2, 2])

for i in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	dp.extend([0] * (n+1-5))
	if dp[n] != 0:
		print(dp[n])
	else:
		for j in range(6, n+1):
			dp[j] = dp[j-1] + dp[j-5]
		print(dp[n])