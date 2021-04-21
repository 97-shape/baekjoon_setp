import sys

x, y, w, h = map(int, sys.stdin.readline().split())

escape = [w-x, h-y, x, y]

print(min(escape))
