
import sys

n = int(sys.stdin.readline()) 
stack = []
k = []

for _ in range(n):
    k = sys.stdin.readline().split()
    if k[0] == '1':
        stack.append(k[1])
    elif k[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif k[0] == '3':
        print(len(stack))
    elif k[0] == '4':
        if stack:
            print('0')
        else:
            print('1')
    elif k[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print('-1')