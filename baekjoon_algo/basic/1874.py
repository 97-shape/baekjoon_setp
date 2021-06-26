import sys

n = int(sys.stdin.readline().rstrip())

stack = []
result = []
count = 1
LIFO = True

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    while count <= num:  # 입력받은 숫자가 나올때까지
        stack.append(count)
        result.append('+')
        count += 1
    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        LIFO = False
if LIFO is False:
    print('NO')
else:
    print('\n'.join(result))
