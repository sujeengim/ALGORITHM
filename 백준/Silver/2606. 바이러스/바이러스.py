# 저장 & 탐색
from collections import deque

n = int(input())
link = int(input())
nlist = [[] for _ in range(n+1)]

for _ in range(link): # 링크 정보 저장
    u, v = map(int, input().split())
    # 양방향 연결 
    nlist[u].append(v)
    nlist[v].append(u)

def bfs(n2, graph): # bfs로 연결을 탐색
    que = deque([1]) # 방문 필요한 장소 저장할 큐
    visited = [False] * (n2+1) # 재탐색 방지
    visited[1] = True

    while que:
        qpop = que.popleft() #하나씩 꺼내서 탐색
        for i in graph[qpop]:
            if not visited[i]: # 방문한 적 없으면 
                visited[i] = True
                que.append(i) # 탐색하기 위해 큐에 추가 
    return visited.count(True) - 1

print(bfs(n, nlist))