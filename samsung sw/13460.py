from collections import deque

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

# 초기 공 위치 파악
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "R":
            rx, ry = i, j
        if arr[i][j] == "B":
            bx, by = i, j
def BFS(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visit = [(rx, ry, bx, by)]
    count = 0
    while q:
        rx, ry, bx, by = q.pop()
        if count > 10:  # 최대 수행횟수 10을 넘을때
            print(-1)
            break
        if arr[rx][ry] == 'O':
            return count
        rdx, rdy = rx, ry
        while True:  # 공이 벽이나 장에물에 부딪히거나 구멍을 지날 때 까지
            for i in range(4):
                rdx += dx[i]
                rdy += dy[i]
                if arr[rdx][rdy] == "#":
                    rdx -= dx[i]
                    rdy -= dy[i]
                    break
                if arr[rdx][rdy] == "O":
                    break
        bdx, bdy = bx, by
        while True:
            for i in range(4):
                bdx += dx[i]
                bdy += dy[i]
                if arr[bdx][bdy] == "#":
                    bdx -= dx[i]
                    bdy -= dy[i]
                    break
                if arr[bdx][bdy] == "O":
                    break
        if arr[bdx][bdy] == "O":  # 파란공이 들어갈 경우(동시에 들어가도 안되기 때문)
            continue
        if rbx == bdx and rby == bdy:  # 공의 좌표가 같을 때
            if abs(rdx-rx) + abs(rdy-ry) > abs(bdx-bx) + abs(bdy-by):  # 이동 거리가 멀다 = 늦게 도착한다.
                rdx -= dx[i]
                rdy -= dy[i]
            else:
                bdx -= dx[i]
                bdy -= dy[i]
        if (rdx, rdy, bdx, bdy) not in visit:
            visit.append((rdx, rdy, bdx, bdy))
    
print(BFS(rx, ry, bx, by))