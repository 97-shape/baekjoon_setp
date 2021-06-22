import sys

n = int(sys.stdin.readline().rstrip())
arr = [0] * 10001  # 1 ~ 10,000 값의 횟수를 셀 리스트 생성


for i in range(n):  # 입력된 값과 일치하는 순번의 리스트 카운트
    a = int(sys.stdin.readline().rstrip())
    arr[a-1] += 1
    
for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            sys.stdout.write(str(i+1) + '\n')
