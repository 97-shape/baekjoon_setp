import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    pair = 0
    ps = sys.stdin.readline().rstrip()
    for j in ps:
        if j == '(':
            pair += 1
        elif j == ')':
            pair -= 1
        if pair < 0:
            print('NO')
            break
    if pair > 0:
        print('NO')
    elif pair == 0:
        print('YES')
        