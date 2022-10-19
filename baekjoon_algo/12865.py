# 냅색 알고리즘

n, k = map(int, input().split())

stuff = [[0, 0]]  # 물건의 무게, 가치
bag = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        # 가방의 최대 무게보다 물건의 무게가 큰 경우
        if j < weight:
            bag[i][j] = bag[i-1][j]
        else:
            # 가방에 들어갈 수 있는 가치의 경우 두 가지
            # 1. 현재 물건의 가치 + 이전 가방의 가치[가방의 최대 무게 - 현재 물건의 무게]
            # 이전 가방의 가치와 비교하는 이유는 같은 물건을 두 번 넣을 수 있기 때문
            # 2. 이전 물건의 가치[현재 가방 무게]
            bag[i][j] = max(value+bag[i-1][j-weight], bag[i-1][j])
print(bag[n][k])