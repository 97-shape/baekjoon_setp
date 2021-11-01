t = int(input())

if t % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = t // 600
    b = t % 600 // 60
    c = t % 600 % 60 // 10 
    print(a, b, c)


"""
t = int(input())

for i in range(3):
    if t == 0:
        break
    if button[i] > t:
        continue
    cnt[i] = t // button[i]
    t %= button[i]

if t == 0:
    print(" ".join(str(cnt[i]) for i in range(3)))
else:
    print(-1)
"""