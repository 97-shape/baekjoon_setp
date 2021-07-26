import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
l = len(nums)
result = []

for i in range(n):
    for j in range(i, l):
        if nums[i] < nums[j]:
            result.append(nums[j])
            break
    if len(result) < i+1:
        result.append(-1)

for i in result:
    print(i, end=' ')