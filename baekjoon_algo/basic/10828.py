import sys

stack = []
order = []

def pop():
    try:
        print(stack.pop(-1))
    except:
        print(-1)

def top():
    try:
        print(stack[-1])
    except:
        print(-1)

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        pop()
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        top()
    