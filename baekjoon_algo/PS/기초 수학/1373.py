import sys
# bin:2진수, oct:8진수. hex:16진수
print(oct(int(sys.stdin.readline().rstrip(), 2))[2:]) # 10진수가 아닌 수를 출력할때 앞 두 자리에 접두어가 붙는다.