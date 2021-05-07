import sys
import numpy as np

def draw_star(n):
    if n == 3:
        canvas[0][:3] = canvas[2][:3] = '*' * 3
        canvas[1][:3] = ['*', ' ', '*']
        return
    k = n // 3
    draw_star(k)  # 가장 작은 크기의 3*3 별 패턴 불려오기 > 가장 큰 크기의 3*3 별 패턴 불려오기
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # canvas[1][1] 즉, 3*3 패턴의 중앙을 파악
                continue
            for a in range(k):  # 3*3 크기의 별 패턴 제작
                canvas[k*i+a][k*j:k*(j+1)] = canvas[a][:k]


n = int(sys.stdin.readline().rstrip())
canvas = [[' ' for m in range(n)] for m in range(n)]

draw_star(n)

for i in canvas:  # 대괄호 없이 어떻게 출력하는가?
    i = np.array(i).flatten().tolist()
    print(i)
