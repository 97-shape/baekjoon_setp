import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    temp = []  # temp 리스트에는 i값 보다 큰 수의 개수가 들어감
    for j in range(i):
        if a[i] < a[j]:
            temp.append(dp[j])
    if not temp:
        continue
    else:
        dp[i] += max(temp)  # 높은 값이 가장 많았던 곳을 기준으로
print(max(dp))