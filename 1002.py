import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    Jo = [], []
    Baek = [0, 0]
    postion = sys.stdin.readline().rsplit()
    Jo.insert(postion[0], postion[1])
    print(Jo)