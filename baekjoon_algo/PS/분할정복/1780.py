import sys
input = sys.stdin.readline

def check(x, y, d):
    global paper
    choice = arr[x][y]
    for i in range(x, x+d):
        for j in range(y, y+d):
            if choice != arr[i][j]:
                dd = d//3
                for ii in range(3):
                    for jj in range(3):
                        check(x + ii*dd, y + jj*dd, dd)
                return
    paper[choice] += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0, 0]
check(0, 0, n)

for i in range(-1, 2):
    print(paper[i])