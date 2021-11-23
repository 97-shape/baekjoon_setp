import sys
input = sys.stdin.readline

n = int(input())
res = abs(100 - n)  # 현재 채널(100)에서 +/- 로만 이동할 경우의 버튼 횟수
m = int(input())
if m:
    broken = list(input().split())
else:
    broken = [-1]

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else:
        #  눌러진 버튼의 횟수(len(str(num))) + (+/-)를 눌러야 하는 횟수
        res = min(res, len(str(num)) + abs(num - n))

print(res)