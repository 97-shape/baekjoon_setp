import sys

# ��Ŭ���� ȣ���� ���
# �ڿ��� a % b = r (a>b)
# a, b�� �ִ����� = b, r �ִ����� 

def gcd(a, b):  # �ִ�����
    while b > 0:
        a, b = b, a%b
    return a

def lmc(a, b):  # �ּҰ����
    return int(a * b / gcd(a, b))

a, b = map(int, sys.stdin.readline().split())

print(gcd(a, b))
print(lmc(a, b))