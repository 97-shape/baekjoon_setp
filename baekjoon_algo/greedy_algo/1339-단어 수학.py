import sys

n = int(sys.stdin.readline())
word = [list(str(sys.stdin.readline().rstrip())) for _ in range(n)]

alpha_dic = {}
alpha_list = []
for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in alpha_dic:  # ��ųʸ� �ȿ� ���ĺ��� ����
            alpha_dic[word[i][j]] += 10 ** (len(word[i]) - j - 1)
        else:  # ��ųʸ� ����
            alpha_dic[word[i][j]] = 10 ** (len(word[i]) - j - 1)

alpha_list = [v for v in alpha_dic.values()]  # �ڸ� ���� ���ĺ��� ��ġ�ϸ� ���ϱ⿡�� �̻��� ����
alpha_list.sort(reverse=True)

sum = 0
pow = 9
for i in range(len(alpha_list)):
    sum += alpha_list[i] * (pow - i)

print(sum)