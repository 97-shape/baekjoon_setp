import sys

def erasto():  # 아리스토텔래스의 채 (미리 완성 > 시간단축)
    Prime_list = [True] * 10000
    for i in range(2, 101):
        if i:
            for j in range(i*i, 10000, i):
                Prime_list[j] = False
    return Prime_list

def check_Goldbach(n):
    Primes = erasto()
    for i in range(n//2, n, 1):  # 중앙 가장 큰 값부터 확인
        if Primes[n-i] and Primes[i]:
            return print(n-i, i)

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    check_Goldbach(n)