import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cnt = 0

# �ּ� �ϳ� �̻��� ���� ������ ����
# k + 3 : ���Ͻ� �����ϴ� �ο� + �� ���� �ο� ��
# n >= 2 and m >= 1 : �� ���ǿ� ���� �ϳ� ���ԵǾ� �����Ƿ� ������ �� ���� �����ο����� ���Ѵ�
while n + m >= k + 3 and n >= 2 and m >= 1:
    cnt += 1
    n -= 2
    m -= 1

print(cnt)