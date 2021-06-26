import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    r_string = []
    string = sys.stdin.readline().split()
    for j in string:
        r_string.append(j[::-1])
    print(' '.join(r_string))