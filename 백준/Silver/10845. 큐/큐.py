#10845
import sys

quelist = []

n = int(input())

for i in range(n):
    cmd = sys.stdin.readline().strip().split()
    cmd0 = cmd[0]

    if cmd0 == 'push':
        quelist.append(int(cmd[1]))
    elif cmd0 == 'pop':
        if quelist:
            print(quelist.pop(0))
        else:
            print(-1)
    elif cmd0 == 'size':
        print(len(quelist))
    elif cmd0 == 'empty':
        if quelist:
            print(0)
        else:
            print(1)
    elif cmd0 == 'front':
        if quelist:
            print(quelist[0])
        else:
            print(-1)
    elif cmd0 == 'back':
        if quelist:
            print(quelist[-1])
        else:
            print(-1)