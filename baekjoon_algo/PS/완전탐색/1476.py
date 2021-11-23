e, s, m = map(int, input().split())

E, S, M, cnt = 1, 1, 1, 1

while True:
    if E == e and S == s and M == m:
        break
    E += 1
    S += 1
    M += 1
    cnt += 1
    if E > 15: E = 1
    if S > 28: S = 1
    if M > 19: M = 1

print(cnt)