total = 36
result = 0

def gcd(x, y):
    while y > 0:
        x, y = y, x%y
    return x

a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

for i in a:
    for j in b:
        if i > j:
            result += 1
        elif i <= j:
            break

t = gcd(total, result)

print("{0}/{1}".format(int(result/t), int(total/t)))