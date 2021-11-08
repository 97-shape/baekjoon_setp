import sys

n = int(sys.stdin.readline())
square = [i * i for i in range(1, n)]

dp = [0] * (n+1)
for i in range(1, n+1):
    temp = []
    if i == 1:
        dp[i] = 1
    else:
        for s in square:
            if s > i:
                break
            temp.append(dp[i-s])
        dp[i] = min(temp) + 1

print(dp[n])