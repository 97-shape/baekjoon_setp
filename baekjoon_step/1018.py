n, m = map(int, input().split())
board = []
result = []

for z in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        b_start = 0
        w_start = 0
        # 위에서 잘라낸 8*8 체스판 검사
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 홀(짝)수번째 칸의 색을 구분 = 순서 구분
                # BWBWBW or WBWBWB 순으로 검사 > 오류시 b(w)_start 개수 추가
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        b_start += 1
                    if board[a][b] != 'W':
                        w_start += 1
                else:
                    if board[a][b] != 'W':
                        b_start += 1
                    if board[a][b] != 'B':
                        w_start += 1
        # 흰(검은)색으로 시작했을 때 칠해야 하는 부분
        result.append(b_start)
        result.append(w_start)

print(min(result))
