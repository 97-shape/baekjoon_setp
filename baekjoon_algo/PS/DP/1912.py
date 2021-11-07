import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = nums[0]
    else:
        dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))