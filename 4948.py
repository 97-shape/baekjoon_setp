import sys

def Prime_list(n):
    Num_list = [True] * (2 * n + 1)
    Num_list[1] = False
    for i in range(2, int((2 * n) ** (1/2))+1):
        if Num_list[i] is True:
            for j in range(i*i, (2 * n) + 1, i):
                Num_list[j] = False
    return [i for i in range(n + 1, (2 * n) + 1) if Num_list[i] is True]

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    print(len(Prime_list(n)))

