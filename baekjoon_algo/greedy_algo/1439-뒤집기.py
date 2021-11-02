import sys

s = str(sys.stdin.readline())
switch = s[0]
zero_one = [0, 0]
temp = ''
for x in s:
    if x != switch:
        zero_one[int(switch)] += 1
        temp = x
        switch = x
    else:
        temp += x

print(min(zero_one))