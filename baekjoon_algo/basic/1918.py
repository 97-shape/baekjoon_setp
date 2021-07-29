import sys

fomula = list(map(str, sys.stdin.readline().rstrip()))
stack = ['']
result = ''

for i in fomula:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            # 연산순위 (우선순위 > 등장 순서)
            while stack and stack[-1] == '*' or stack[-1] == '/':
                result += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            # 괄호를 제외한 연산순위 높은 연산자 pop
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # '(' 제거
while stack:
    result += stack.pop()
print(result)
