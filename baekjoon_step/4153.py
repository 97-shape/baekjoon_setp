import sys

while True:
    length = list(map(int, sys.stdin.readline().split()))
    if length.count(0) == 3:
        break
    heru = length.pop(length.index(max(length)))
    if pow(heru, 2) == pow(length[0], 2) + pow(length[1], 2):
        print("right")
    else:
        print("wrong")
