import sys

nums = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    nums[int(sys.stdin.readline())] += 1

for i in range(10001):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)
