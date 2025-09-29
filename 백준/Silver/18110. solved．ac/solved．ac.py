import sys

n = int(input().strip())
if n == 0:
    print(0)
else:
    m = int(n * 0.15 + 0.5)
    # print(m)
    levels = sorted([int(sys.stdin.readline().strip()) for x in range(n)])
    # print(levels)
    levels = levels[m:n-m]
    # print(levels)
    print(int((sum(levels)/len(levels))+0.5))
