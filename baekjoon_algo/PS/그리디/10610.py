n = list(input())
n.sort(reverse=True)  # 30의 배수가 되는 가장 큰 수
sum = 0

for i in n:
	sum += int(i)
if sum%3 != 0 or not '0' in n:  # 3의 배수 : 각 자리수의 합 % 3 = 0
	print(-1)
else:
	print(''.join(n))