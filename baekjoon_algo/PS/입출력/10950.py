import sys

while True:
    try:  # try ���ο� �ִ� �ڵ带 ����
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:  # try ���ο� �ִ� �ڵ忡 �̻��� ������ ����
        break
