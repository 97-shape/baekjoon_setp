import sys
input = sys.stdin.readline

def merge_sort(arr):
    def divid(s, e):
        if e - s < 2:
            return
        m = (s+e) // 2
        divid(s, m)
        divid(m, e)
        merge(s, m, e)

    def merge(start, mid, end):
        global cnt
        temp = []
        s, e = start, mid

        while s < mid and e < end:
            if arr[s] > arr[e]:
                temp.append(arr[e])
                e += 1
                cnt += (mid - s)  # 교환값 = 남아있는 좌측 항목의 갯수
            else:
                temp.append(arr[s])
                s += 1
                
        while s < mid:
            temp.append(arr[s])
            s += 1
        while e < end:
            temp.append(arr[e])
            e += 1

        for i in range(start, end):
            arr[i] = temp[i-start]
    
    return divid(0, len(arr))


n = int(input())
a = list(map(int, input().split()))
cnt = 0
merge_sort(a)
print(cnt)