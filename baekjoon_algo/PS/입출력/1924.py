import sys

x, y = map(int, sys.stdin.readline().split())

res = 0
for i in range(x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        res += 31
    elif i in [4, 6, 9, 11]:
        res += 30
    elif i == 2:
        res += 28

day = (res + y) % 7

if day == 0:
    print("SUN")
elif day == 1:
    print("MON")
elif day == 2:
    print("TUE")
elif day == 3:
    print("WED")
elif day == 4:
    print("THU")
elif day == 5:
    print("FRI")
elif day == 6:
    print("SAT")