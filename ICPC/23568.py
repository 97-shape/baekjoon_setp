import sys
input = sys.stdin.readline
move = dict()

n = int(input())
for _ in range(n):
    s, d, m = input().split()
    move[int(s)] = [d, int(m)]

start = int(input())
while True:
    if move[start][0] == "L":
        start -= move[start][1]
    else:
        start += move[start][1]

print(start)
