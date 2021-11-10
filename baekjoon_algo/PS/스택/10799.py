import sys

sticks = list(sys.stdin.readline().rstrip())
stack = []
result = 0

for i in range(len(sticks)):
    if sticks[i] == '(':
        stack.append('(')
    else:
        if sticks[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)