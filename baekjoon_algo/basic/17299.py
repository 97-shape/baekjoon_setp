import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

result = ['-1'] * n
count = {}
stack = [0]  # index값 저장

for num in nums:
    try:
        count[num] += 1
    except:
        count[num] = 1

for i in range(1, n):  # stack에 n개의 수 index 입력
    while stack and count[nums[stack[-1]]] < count[nums[i]]:
        result[stack.pop()] = str(nums[i])
    stack.append(i)

print(" ".join(result))

