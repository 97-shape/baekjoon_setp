import sys

nums = []
for i in range(int(sys.stdin.readline())):
	nums.append(int(sys.stdin.readline()))

nums.sort()

for n in nums:
	print(n)