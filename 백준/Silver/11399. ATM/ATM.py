n = int(input())
nlist = list(map(int, input().strip().split()))
nlist.sort()
s = 0

for i in range(n):
    s += sum(nlist[0:i+1])

print(s)