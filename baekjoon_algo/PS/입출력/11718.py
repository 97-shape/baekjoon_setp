while True:
    try:
        print(input())  # sys.stdin.redline()�� EOFError�� �������� �ʰ� ������ �����Ѵ�
    except EOFError:  # �Է��� ��� ������ �߻��� �� (EOFError) 
        break