import sys

# String변수로 받은걸 다시 cursor_L로 받지 않아도 됨(출력초과 이유?)
cursor_L = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline().rstrip())
cursor_R = []

# insert, del을 쓰지않는 이유
# 둘다 O(N)으로 시간복잡도가 O(1)인 append, pop보다 크기 때문

for i in range(n):
    commend = sys.stdin.readline().split()
    if commend[0] == 'L' and len(cursor_L) != 0:
        cursor_R.append(cursor_L.pop())
    elif commend[0] == 'D' and len(cursor_R) != 0:
        cursor_L.append(cursor_R.pop())
    elif commend[0] == 'B' and len(cursor_L) != 0:
        cursor_L.pop()
    elif commend[0] == 'P':
        cursor_L.append(commend[1])

# 뒤집는 이유 : 커서 우측의 문장들은 역순으로 받아서
print(''.join(cursor_L + list(reversed(cursor_R))))
