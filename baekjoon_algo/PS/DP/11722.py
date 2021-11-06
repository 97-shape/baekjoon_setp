import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    temp = []  # temp ����Ʈ���� i�� ���� ū ���� ������ ��
    for j in range(i):
        if a[i] < a[j]:
            temp.append(dp[j])
    if not temp:
        continue
    else:
        dp[i] += max(temp)  # ���� ���� ���� ���Ҵ� ���� ��������
print(max(dp))