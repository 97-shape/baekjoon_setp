import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0]

dp.append(wine[0])
if n > 1:
    dp.append(wine[0] + wine[1])
for i in range(3, n+1):
    # �������
    # 1. ���� ������ �����ָ� ���� ���� ���
    # 2. ���ݰ� ���� ������ �����ָ� �Ծ��� ���
    # 3. ������ �Ե� ���� ������ �����ָ� ���� ���� ���
    dp.append(max(dp[i-1], dp[i-3] + wine[i-1] + wine[i-2] ,wine[i-1] + dp[i-2]))

print(dp[n])