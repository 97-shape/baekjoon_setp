import sys

# f : first, l : last. m : middle
def merge_sort(arr):
    def sort(f, l):
        if l - f < 2:  # 끝 - 시작 < 2 == 더이상 나눌 수 없음. 즉, 정렬이 끝남
            return
        m = (f+l)//2
        # 시작에서 중간 / 중간에서 끝까지를 분열
        sort(f, m)
        sort(m, l)
        merge(f, l, m)

    def merge(f, l, m):
        temp = []
        F, M = f, m

        # F < m : False(F배열의 값이 없을때) or M<l : False(l배열의 값이 없을때) 까지 정렬
        while F < m and M < l:
            if arr[F] < arr[M]:
                temp.append(arr[F])
                F += 1
            else:
                temp.append(arr[M])
                M += 1

        # 위 반복문이 끝난 후 나머지 정리하기(이미 정렬된 상태라서 그대로 삽입)
        while F < m:
            temp.append(arr[F])
            F += 1
        while M < l:
            temp.append(arr[M])
            M += 1

        for i in range(f, l):  # 정렬된 내용을 삽입
            arr[i] = temp[i-f]

    return sort(0, len(arr))  # 정렬 함수 실행

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

merge_sort(arr)
print(arr)
