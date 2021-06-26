import sys

n = int(sys.stdin.readline().rstrip())

people_info = []

for i in range(n):
    people_info.append(list(map(int, sys.stdin.readline().split())))

for i in people_info:
    rank = 1
    for j in people_info:
        if i[0] < j[0] and i[1] < j[1]:  # 본인 포함 모든 값 비교계산(단순)
            rank += 1
    print(rank, end=' ')
