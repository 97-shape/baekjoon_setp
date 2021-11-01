import sys

n = int(sys.stdin.readline())
word = [list(str(sys.stdin.readline().rstrip())) for _ in range(n)]

alpha_dic = {}
alpha_list = []
for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in alpha_dic:  # 딕셔너리 안에 알파벳이 존재
            alpha_dic[word[i][j]] += 10 ** (len(word[i]) - j - 1)
        else:  # 딕셔너리 생성
            alpha_dic[word[i][j]] = 10 ** (len(word[i]) - j - 1)

alpha_list = [v for v in alpha_dic.values()]  # 자리 값과 알파벳이 일치하면 더하기에는 이상이 없음
alpha_list.sort(reverse=True)

sum = 0
pow = 9
for i in range(len(alpha_list)):
    sum += alpha_list[i] * (pow - i)

print(sum)