import sys

n = int(sys.stdin.readline())

fomula = list(map(str, sys.stdin.readline().rstrip()))
nums = [0] * n
stack = []
for i in range(n):
    nums[i] = int(sys.stdin.readline())

for i in fomula:
    if i.isalpha():  # isalpha : 알파벳 인지 확인
        # ord: 유니코드 값 반환
        # A, B, C 순서로 nums 리스트의 값들을 스택에 저장
        stack.append(nums[ord(i) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '*':
            stack.append(num1 * num2)
        elif i == '/':
            stack.append(num1 / num2)

print('%.2f' % stack.pop())
