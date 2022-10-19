arr = []
for _ in range(int(input())):
    i = int(input())
    if i == 0:
        arr.pop()
    else:
        arr.append(i)
print(sum(arr))