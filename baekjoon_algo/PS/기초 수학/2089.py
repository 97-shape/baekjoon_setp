import sys

def trans(n):
    if n == 0:
        return '0'
    else:
        if n % 2 == 0:
            return trans(n//-2) + '0'
        else:
            return trans(n//-2 + 1) + '1' # nÀÌ È¦¼ö: n // k  = 0 or -1

t = int(sys.stdin.readline())
res = trans(t)
if res == '0':
    print(res)
else:
    print(res[1:])