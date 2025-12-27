import sys
from collections import deque
deq = deque()
N = int(sys.stdin.readline().strip())
for _ in range(N):
    req = sys.stdin.readline().strip().split() #리스트 생성
    if len(req) >= 2:
        command, value = req[0], int(req[1])
        if command == 'push_front':
            deq.appendleft(value)
        elif command == 'push_back':
            deq.append(value)
    else:
        command = req[0]
        if command == 'pop_front':
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        elif command == 'pop_back':
            if deq:
                print(deq.pop())
            else:
                print(-1)
        elif command == 'size':
            print(len(deq))
        elif command == 'empty':
            if deq:
                print(0)
            else:
                print(1)
        elif command == 'front':
            if deq:
                print(deq[0])
            else:
                print(-1)
        elif command == 'back':
            if deq:
                print(deq[-1])
            else:
                print(-1)