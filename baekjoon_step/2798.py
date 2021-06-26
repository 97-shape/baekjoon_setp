import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

black_Jack = 0

for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                # 저장된 값과 조건에 부합한 값의 최대값(max)을 저장함
                black_Jack = max(black_Jack, card[i] + card[j] + card[k])

print(black_Jack)
