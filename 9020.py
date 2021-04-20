import sys

def erasto(n):
    Prime_list = [True] * n
    for i in range(2, int(n ** (1/2))+1):
        if i:
            for j in range(i*i, n, i):
                Prime_list[j] = False
    return [i for i in range(2, n) if Prime_list[i] is True]

def check_Goldbach(n):
    Primes = erasto(n)
    sub = 0
    for i in Primes:
        if Primes.count(n-i) == 1 and sub <= n-(2*i):
            a = i
            b = n-i
    return print(a, b)

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    check_Goldbach(n)
