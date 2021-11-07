import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * n

dp[0] = s[0]
if n >= 2:
    dp[1] = max(s[0] + s[1], s[1])
if n >= 3:
    dp[2] = max(s[0] + s[2], s[1] + s[2])
for i in range(3, n):
    dp[i] = max(s[i] + dp[i-2], dp[i-3] + s[i] + s[i-1])

print(dp[n-1])