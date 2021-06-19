import sys

n = int(sys.stdin.readline().rstrip())
num = []

for z in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

# 버블 정렬
roop = n-1
for i in range(roop):
    for j in range(roop-i):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

for z in range(n):
    print(num[z])
