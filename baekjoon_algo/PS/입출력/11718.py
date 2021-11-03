while True:
    try:
        print(input())  # sys.stdin.redline()은 EOFError를 리턴하지 않고 공백을 리턴한다
    except EOFError:  # 입력이 없어서 오류가 발생할 때 (EOFError) 
        break