import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            # dp[i][j] = 1 틀린 이유 : 만약 i = 4 일때 뒷자리가 0이 될 경우는 1010, 1210 2가지 즉, dp[i-1][1] 값과 같다.
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)