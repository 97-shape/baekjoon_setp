import sys

card = {}

for _ in range(int(sys.stdin.readline())):
    c = int(sys.stdin.readline())
    if c in card:
        card[c] += 1
    else:
        card[c] = 1

card = sorted(card.items(), key=lambda card: (-card[1], card[0]))  # dic 정렬은 sorted를 쓴다
print(card[0][0])