import sys

def count(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

n, m = map(int, sys.stdin.readline().split())

# 0의 개수 = 10의 배수 = 2와 5의 승수 중 최솟값
# https://st-lab.tistory.com/166
print(min(count(n, 2) - count(n-m, 2) - count(m, 2), count(n, 5) - count(n-m, 5) - count(m, 5)))