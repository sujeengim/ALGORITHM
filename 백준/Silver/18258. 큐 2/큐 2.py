import sys
from collections import deque

N = int(sys.stdin.readline().strip()) #sys
que = deque()
for _ in range(N):
    command = sys.stdin.readline().strip().split() #sys, 결과는 리스트
    if len(command)>1:
        command, val = command
        que.append(int(val))
    else:
        command = command[0]
        if command=='pop':
            if len(que)<=0:
                print(-1)
            else:
                print(que.popleft())
        elif command=='size':
            print(len(que))
        elif command=='empty':
            if len(que)<=0:
                print(1)
            else:
                print(0)
        elif command=='front':
            if len(que)<=0:
                print(-1)
            else:
                print(que[0])
        elif command=='back':
            if len(que)<=0:
                print(-1)
            else:
                print(que[-1])