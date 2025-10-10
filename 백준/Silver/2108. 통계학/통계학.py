import sys, math
from collections import Counter

n = int(input())
nlist = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

print(math.floor((sum(nlist)/n)+0.5)) #산술평균
print(nlist[n//2]) #중앙값

#최빈값
cnt = dict(Counter(nlist)) 
filter_cnt = {}

for k, v in cnt.items():
    if v == max(cnt.values()):
        filter_cnt.update({k:v})

if len(filter_cnt) > 1:#최빈값이 여러개면 두번째로 작은 값
    filter_cnt = sorted(filter_cnt)[1:] #최소값 제거 
    print(filter_cnt[0])#그다음 최소값 출력 
else:#최빈값이 하나면 그 값
    print(list(filter_cnt.keys())[0]) 

# 범위 
print(nlist[-1]-nlist[0])