import sys
n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(sys.stdin.readline().strip()))
newlist = []
for i in range(len(nlist)-1):
    newlist.append(nlist[i+1]-nlist[i])

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

gcd_value = newlist[0]
for i in range(1, len(newlist)):
    gcd_value = gcd(gcd_value, newlist[i])

ans = (nlist[-1] - nlist[0]) // gcd_value + 1 - n
print(ans)
