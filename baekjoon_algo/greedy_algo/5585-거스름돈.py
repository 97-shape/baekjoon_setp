coin = [500, 100, 50, 10, 5, 1]

n = int(input())

change = 1000 - n

cnt = 0
for i in coin:    
    if  change == 0:
        break
    if i > change:
        continue
    cnt += change // i
    change %= i

print(cnt)