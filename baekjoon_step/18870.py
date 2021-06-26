import sys

n = int(sys.stdin.readline().rstrip())

x = list(map(int, sys.stdin.readline().split()))


x_set = sorted(list(set(x)))  # 중복 제거, 오름차순 정렬 : 조건을 만족하는 좌표의 개수 == index값

x_dic = {x_set[i]: i for i in range(len(x_set))}  # 딕서너리 타입을 이용, 각 항목의 순서를 저장

for i in x:
    print(x_dic[i], end=' ')
