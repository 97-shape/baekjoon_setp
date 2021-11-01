import sys

n = int(sys.stdin.readline())

meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
meeting.sort(key=lambda x:(x[1], x[0]))

cnt = 0
last_t = 0

for i in range(n):
    if meeting[i][0] >= last_t:
        cnt += 1
        last_t = meeting[i][1]

print(cnt)