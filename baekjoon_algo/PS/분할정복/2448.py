import sys
import math
input = sys.stdin.readline

def draw(v):
    l = len(star)
    for i in range(l):
        star.append(star[i] + star[i])
        star[i] = ("   " * v + star[i] + "   " * v)  # v�� = ���� ����, ���� ���� ��ŭ ���� ����
        

star = ['  *   ', ' * *  ', '***** ']  # ***** ���ο��� ��ĭ ������ ���������� ��� �׸� �ڿ� ���� �߰�

n = int(input())
k = int(math.log(int(n/3), 2))  # n = 3 * (2**k)
for i in range(k):
    draw(int(pow(2,i)))  # v : ������ �� n = 3, v = 0, n = 6, v = 3 * (2**0), n = 12, v = 3 * (2**1)
for i in star:
    print(i)