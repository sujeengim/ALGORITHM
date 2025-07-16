import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
nlist = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
mlist = list(map(int, sys.stdin.readline().strip().split()))

n_counts = Counter(nlist)

results = []
for i in mlist:
    results.append(str(n_counts[i])) 

print(' '.join(results))