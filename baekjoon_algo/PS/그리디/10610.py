n = list(input())
n.sort(reverse=True)  # 30�� ����� �Ǵ� ���� ū ��
sum = 0

for i in n:
	sum += int(i)
if sum%3 != 0 or not '0' in n:  # 3�� ��� : �� �ڸ����� �� % 3 = 0
	print(-1)
else:
	print(''.join(n))