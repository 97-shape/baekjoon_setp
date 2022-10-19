import heapq
import sys
n = int(sys.stdin.readline())
left_heapq = []  # 최대 힙
right_heapq = []  # 최소 힙

for _ in range(n):
    num = int(sys.stdin.readline())

    # 길이가 같다 = 짝수 = 수를 추가하면 홀수가 된다 = 중간값을 최대힙에
    if len(left_heapq) == len(right_heapq):
        heapq.heappush(left_heapq, -num)
    else:
        heapq.heappush(right_heapq, num)

    # 우측과 좌측값을 비교하여 중간값이 될 수 있는 두 값중 작은 값을 최대 힙 다른 값을 최소힙으로 옮겨준다.
    if right_heapq and right_heapq[0] < -left_heapq[0]:
        l = heapq.heappop(left_heapq)
        r = heapq.heappop(right_heapq)

        heapq.heappush(left_heapq, -r)
        heapq.heappush(right_heapq, -l)
    
    print(-left_heapq[0])