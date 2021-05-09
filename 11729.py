import sys

def hanoi(n, start, via, end):
    if n == 1:  # 'start' 막대에 있는 가장 작은 원판을 'end' 막대로
        logs.append([start, end])
    else:
        hanoi(n-1, start, end, via)
        logs.append([start, end])
        hanoi(n-1, via, start, end)

n = int(sys.stdin.readline().rstrip())
logs = []  # list 안쓰는 방법이 있을까?

hanoi(n, 1, 2, 3)
print(len(logs))
print('\n'.join([' '.join(str(i) for i in log) for log in logs]))
