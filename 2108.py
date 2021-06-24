import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []

for i in range(n):
    a = int(sys.stdin.readline())
    num.append(a)

num.sort()
# most_common() : 등장한 횟수를 내림차순으로 정리(빈도 多 > 少)
num_cnt = Counter(num).most_common()


print(round(sum(num)/n))

# 중앙값
print(num[n//2])

# 최빈값
if len(num_cnt) > 1:
    if num_cnt[0][1] == num_cnt[1][1]:
        print(num_cnt[1][0])
    else:
        print(num_cnt[0][0])
else:
    print(num_cnt[0][0])

print(num[-1] - num[0])  # 리스트명[-1] : 리스트의 최대값
