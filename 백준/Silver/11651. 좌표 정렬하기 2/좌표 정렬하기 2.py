import sys 
n = int(input())
nlist = []
for _ in range(n):
    m = list(map(int, sys.stdin.readline().strip().split()))
    nlist.append(m)

nlist.sort(key=lambda x: (x[1],x[0]))
for v in nlist:
    print(*(v), sep=' ')