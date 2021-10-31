import sys

def merge_sort(arr):
	if len(arr) < 2:
		return arr
	
	m = len(arr) // 2

	low_merge = merge_sort(arr[:m])
	high_merge = merge_sort(arr[m:])

	merged_arr = []
	l = h = 0
	while l < len(low_merge) and h < len(high_merge):
		if low_merge[l] > high_merge[h]:
			merged_arr.append(high_merge[h])
			h += 1
		else:
			merged_arr.append(low_merge[l])
			l += 1
	
	merged_arr += low_merge[l:]
	merged_arr += high_merge[h:]

	return merged_arr

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))

merged = merge_sort(p)

temp = 0
res = 0
for i in merged:
	temp += i
	res += temp

print(res)