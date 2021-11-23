import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cnt = 0

# 최소 하나 이상의 팀을 가지는 조건
# k + 3 : 인턴쉽 참여하는 인원 + 한 팀의 인원 수
# n >= 2 and m >= 1 : 위 조건에 팀이 하나 포함되어 있으므로 범위를 한 팀의 구성인원으로 정한다
while n + m >= k + 3 and n >= 2 and m >= 1:
    cnt += 1
    n -= 2
    m -= 1

print(cnt)