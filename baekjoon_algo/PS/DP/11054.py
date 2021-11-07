import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
reverse_a = a[::-1]

u_dp = [1] * n
d_dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            u_dp[i] = max(u_dp[i], u_dp[j] + 1)
        if reverse_a[i] > reverse_a[j]:
            d_dp[i] = max(d_dp[i], d_dp[j] + 1)

res = 0
for i in range(n):
    sum = u_dp[i] + d_dp[n-1-i]
    if sum > res:
        res = sum

print(res-1)  # res - 1 하는 이유 : 가장 긴 수열의 최대값을 두번 포함하기 때문에