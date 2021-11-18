import sys


prime = [True] * (1000001)
def prime_list(n):
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i+i, n+1, i):
                prime[j] = False

prime_list(1000000)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    flag = 1

    for i in range(3, n+1):
        if prime[i] and prime[n-i]:
            print("{0} = {1} + {2}".format(n, i, n-i))
            flag = 0
            break
    
    if flag:
        print("Goldbach's conjecture is wrong.")
