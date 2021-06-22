import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
num = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    num.append(a)

num.sort()
num_cnt = Counter(num).most_common()  #most_common() : 등장한 횟수를 내림차순으로 정리(빈도 多 > 少)

print(round(sum(num)/n))
print(num[n//2])
print(num_cnt)

