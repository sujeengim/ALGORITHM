# DP

T = int(input())

def d(n):
    tlist = [0, 1,2,4] + [0 for _ in range(n-3)] 
    for i in range(4, n+1):
        tlist[i] = tlist[i-1] + tlist[i-2] + tlist[i-3]
    return tlist[n]

for _ in range(T):
    n = int(input())
    if n<=3:
        if n==1:
            print(1)
        elif n==2:
            print(2)
        elif n==3:
            print(4)
    else:
        print(d(n))
