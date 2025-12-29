import sys, heapq
heap = []
N = int(sys.stdin.readline().strip()) #sys
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if n<=0:
        if len(heap)<=0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -n)