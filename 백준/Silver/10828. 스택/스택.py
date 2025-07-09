# 10828
import sys

intstack = []

n = int(input())

for i in range(n):
    cmd = sys.stdin.readline().strip().split() #리스트 반환
    cmd0 = cmd[0]

    if cmd0 == 'push':
        intstack.append(cmd[1])
    elif cmd0 == 'pop': # 맨위 출력후 삭제 
        if len(intstack)==0:
            print(-1)
        else:
            print(intstack.pop(-1))
    elif cmd0 == 'size':
        print(len(intstack))
    elif cmd0 == 'empty':
        if len(intstack)==0:
            print(1)
        else:
            print(0)
    elif cmd0 == 'top': # 맨위 출력만
        if len(intstack)==0:
            print(-1)
        else:
            print(intstack[-1])

