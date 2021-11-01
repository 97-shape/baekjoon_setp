
formula = input().split('-')

f = []
for x in formula:
    sum = 0
    nums = x.split('+')
    for num in nums:
        sum += int(num)
    f.append(sum)

res = f[0]
for i in range(1, len(f)):
    res -= f[i]

print(res)