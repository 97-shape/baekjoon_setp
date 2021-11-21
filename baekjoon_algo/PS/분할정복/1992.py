import sys
input = sys.stdin.readline

def quad(x, y, d):
    if d == 1:
        return str(arr[x][y])
    temp = []
    for i in range(x, x+d):
        for j in range(y, y+d):
            if arr[x][y] != arr[i][j]:
                temp.append('(')
                # extend : ����Ʈ ���� ���� �ٱ��� iterable�� ��� �׸��� ������
                # a = [1, 2] b = [2, 3] a.extend(b) > a = [1, 2, 3, 4]
                temp.extend(quad(x, y, d//2)) # 2��и�
                temp.extend(quad(x, y + d//2, d//2)) # 1��и�
                temp.extend(quad(x + d//2, y, d//2)) # 3��и�
                temp.extend(quad(x + d//2, y + d//2, d//2)) # 4��и�
                temp.append(')')
                return temp
                
    return str(arr[x][y])

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

print(''.join(quad(0, 0, n)))
