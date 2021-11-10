import sys

for _ in range(int(sys.stdin.readline())):
    stack = 0
    ps = sys.stdin.readline().rstrip()
    for p in ps:
        if p == '(':
            stack += 1
        elif p == ')':
            stack -= 1
        
        if stack < 0:
            print('NO')
            break
    if stack > 0:
        print('NO')
    elif stack == 0:
        print('YES')

