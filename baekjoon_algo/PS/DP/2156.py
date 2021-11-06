import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0]

dp.append(wine[0])
if n > 1:
    dp.append(wine[0] + wine[1])
for i in range(3, n+1):
    # 순서대로
    # 1. 지금 차례의 포도주를 먹지 않은 경우
    # 2. 지금과 이전 차례의 포도주를 먹었는 경우
    # 3. 지금은 먹되 이전 차례의 포도주를 먹지 않은 경우
    dp.append(max(dp[i-1], dp[i-3] + wine[i-1] + wine[i-2] ,wine[i-1] + dp[i-2]))

print(dp[n])