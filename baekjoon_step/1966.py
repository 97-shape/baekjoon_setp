for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))

    count = 0
    while q:
        count += 1
        temp = q.popleft()
        if temp == n:
            
