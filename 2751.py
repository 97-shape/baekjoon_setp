import sys

n = int(sys.stdin.readline().rstrip())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

for i in sorted(arr):  # 파이썬 기본 정렬함수
    print(i)