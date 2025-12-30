# 음수와 양수를 따로 관리 
import sys, heapq
heapp = [] #plus
heapm = [] #minus
N = int(sys.stdin.readline().strip())
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    # print(f'{heapp if heapp else "[]"}, {heapm if heapm else "[]"}')
    if n==0:
        #최소 출력
        if not heapp and not heapm:
            print(0)
        else:
            p = heapp[0] if heapp else float('inf') # 힙 비어있으면 무한대로 처리
            m = heapm[0] if heapm else float('inf')
            if p>m: #p의 절댓값이 더 클때 
                print(-heapq.heappop(heapm))
            elif p<m: #m의 절댓값이 더 클때
                print(heapq.heappop(heapp))
            elif p==m:
                print(-heapq.heappop(heapm))
    elif n>0:
        heapq.heappush(heapp, n)
    else:
        heapq.heappush(heapm, -n)