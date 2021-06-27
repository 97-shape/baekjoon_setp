import sys
import collections  # collections.deque 사용하기 위해 임포트

'''
deque : double-ended queue
양방향에서 데이터를 처리할 수 있는 queue형 자료구조

출처: https://excelsior-cjh.tistory.com/96 [EXCELSIOR]
'''

def push(position, num):
    if position == 'back':
        Deque.append(num)
    elif position == 'front':
        Deque.appendleft(num)  # 앞부터 추가(기본: 뒤)

Deque = collections.deque([])  # 리스트와 흡사함
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    commend = sys.stdin.readline().split()
    if commend[0] == 'push_back':
        push('back', commend[1])
    elif commend[0] == 'push_front':
        push('front', commend[1])
    elif commend[0] == 'pop_front':  # 앞부터 제거(기본: 뒤)
        try:
            print(Deque.popleft())
        except IndexError:
            print(-1)
    elif commend[0] == 'pop_back':
        try:
            print(Deque.pop())
        except IndexError:
            print(-1)
    elif commend[0] == 'size':
        print(len(Deque))
    elif commend[0] == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        try:
            print(Deque[0])
        except IndexError:
            print(-1)
    elif commend[0] == 'back':
        try:
            print(Deque[-1])
        except IndexError:
            print(-1)
