import sys

s = sys.stdin.readline().rstrip()

for x in s:
    if x.isupper():
        if ord(x) + 13 <= 90:
            print(chr(ord(x) + 13), end='')
        else:
            print(chr(ord(x) - 13), end='')
    elif x.islower():
        if ord(x) + 13 <= 122:
            print(chr(ord(x) + 13), end='')
        else:
            print(chr(ord(x) - 13), end='')
    else:
        print(x, end='')