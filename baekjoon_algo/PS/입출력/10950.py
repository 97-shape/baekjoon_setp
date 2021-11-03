import sys

while True:
    try:  # try 내부에 있는 코드를 실행
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:  # try 내부에 있는 코드에 이상이 있을때 실행
        break
