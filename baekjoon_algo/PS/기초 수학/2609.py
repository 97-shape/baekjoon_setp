import sys

# 유클리드 호제법 사용
# 자연수 a % b = r (a>b)
# a, b의 최대공약수 = b, r 최대공약수 

def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a%b
    return a

def lmc(a, b):  # 최소공배수
    return int(a * b / gcd(a, b))

a, b = map(int, sys.stdin.readline().split())

print(gcd(a, b))
print(lmc(a, b))