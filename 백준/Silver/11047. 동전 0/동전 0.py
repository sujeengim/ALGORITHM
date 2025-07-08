#11047
import sys

n, k = map(int, input().strip().split())
nlist = []  # 동전 종류
gap = k
cnt = 0

for i in range(n):
    na = int(sys.stdin.readline().strip())
    nlist.append(na)

nlist.sort(reverse=True)  

for i in range(len(nlist)):
    if gap==0:
        break
    cnt += (gap//nlist[i])
    gap = gap%nlist[i]


print(cnt)
