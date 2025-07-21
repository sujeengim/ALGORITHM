import sys
n = int(input().strip())
tlist = list(map(int, sys.stdin.readline().strip().split()))
t,  p = map(int, input().strip().split())

tcount = 0
for i in tlist:
    if i % t == 0:
        tcount += (i // t)
    else:
        tcount += (i//t + 1)
    
print(tcount)
print(n//p, n%p)