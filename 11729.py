import sys

def hanoi(n, start, via, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, via)
        print(start, via)
        


n = int(sys.stdin.readline().rstrip())


