n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)

max_w = 0

for i in range(1, n+1):
    p_w = i * rope[i-1]
    if p_w > max_w:
        max_w = p_w

print(max_w)