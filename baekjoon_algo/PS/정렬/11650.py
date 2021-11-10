import sys

grid = []

for i in range(int(sys.stdin.readline())):
    grid.append(list(map(int, sys.stdin.readline().split())))

grid.sort(key=lambda grid:(grid[0], grid[1]))

for g in grid:
    for x in g:
        print(x, end=' ')
    print()