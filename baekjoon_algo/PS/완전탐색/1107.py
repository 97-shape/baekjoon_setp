import sys
input = sys.stdin.readline

n = int(input())
res = abs(100 - n)  # ���� ä��(100)���� +/- �θ� �̵��� ����� ��ư Ƚ��
m = int(input())
if m:
    broken = list(input().split())
else:
    broken = [-1]

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else:
        #  ������ ��ư�� Ƚ��(len(str(num))) + (+/-)�� ������ �ϴ� Ƚ��
        res = min(res, len(str(num)) + abs(num - n))

print(res)