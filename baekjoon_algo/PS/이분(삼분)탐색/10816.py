import sys
# bisect ÇÔ¼ö¶õ : https://velog.io/@woo0_hooo/python-Bisect-%ED%95%A8%EC%88%98%EB%9E%80
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for i in range(m):
	print(bisect_right(a, b[i]) - bisect_left(a, b[i]), end = ' ')
