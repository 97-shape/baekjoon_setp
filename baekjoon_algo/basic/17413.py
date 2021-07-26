import sys

s = sys.stdin.readline().strip('\n')
tag = False
string = ''
result = ''

for i in s:
    if tag is False:
        if i == '<':
            tag = True
            string += i
        elif i == ' ':
            string += i
            result += string
            string = ''
        else:
            string = i + string
    elif tag is True:
        string += i
        if i == '>':
            tag = False
            result += string
            string = ''

print(result + string)
