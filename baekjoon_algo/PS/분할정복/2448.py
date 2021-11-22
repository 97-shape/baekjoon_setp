import sys
import math
input = sys.stdin.readline

def draw(v):
    l = len(star)
    for i in range(l):
        star.append(star[i] + star[i])
        star[i] = ("   " * v + star[i] + "   " * v)  # v값 = 줄의 길이, 줄의 길이 만큼 공백 증가
        

star = ['  *   ', ' * *  ', '***** ']  # ***** 서로에게 한칸 공백이 존재함으로 모든 항목 뒤에 공백 추가

n = int(input())
k = int(math.log(int(n/3), 2))  # n = 3 * (2**k)
for i in range(k):
    draw(int(pow(2,i)))  # v : 공백의 수 n = 3, v = 0, n = 6, v = 3 * (2**0), n = 12, v = 3 * (2**1)
for i in star:
    print(i)