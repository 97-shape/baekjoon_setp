import sys

n = int(sys.stdin.readline().rstrip())

q = []

for i in range(n):
    commend = sys.stdin.readline().split()
    if commend[0] == 'push':
        q.append(commend[1])
    elif commend[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif commend[0] == 'size':
        print(len(q))
    elif commend[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif commend[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
