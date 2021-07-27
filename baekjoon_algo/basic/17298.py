import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

result = [-1] * n
stack = [0]

for i in range(1, n):
    # stack에 nums[i]보다 작은 모든 값을 pop함
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)

for j in result:
    print(j, end=' ')