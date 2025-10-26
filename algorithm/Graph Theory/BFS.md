<img width="554" height="292" alt="image" src="https://github.com/user-attachments/assets/0b238830-cceb-4d96-94de-2aa01d33459d" />

### BFS : 너비 우선 탐색 
#### 시작점에서 가까운 노드부터 수평적으로 탐색합니다. (큐 사용)

그래프 탐색에서 신경쓸 부분은
저장이다.

방문을 놓치는 곳이 없도록 
탐색할 곳을 저장해두어야 한다. 
또 재방문은 하지않도록
방문한 곳 저장을 잘 해두어야 한다. 


```python
from collections import deque

def bfs(graph, start_node):
    visited = [False] * len(graph) # 방문한 곳 저장
    queue = deque([start_node])  # 방문할 곳 저장
    
    visited[start_node] = True

    while queue:
        v = queue.popleft() #하나씩 꺼내서 탐색시작
        
        for neighbor in graph[v]: 
            if not visited[neighbor]: # 방문한 적 없으면 
                visited[neighbor] = True
                queue.append(neighbor) # 큐에 추가해서 탐색

# 예시 그래프 
graph = [
    [],
    [2, 3], # 대부분 1번부터 사용하기에 
    [1, 7],
    [1, 4, 5],
    [3, 6],
    [3, 7],
    [4, 8],
    [2, 5, 8],
    [6, 7]
]

bfs(graph, 1)
# 예상 출력: 1 2 3 7 4 5 8 6
```
<hr/>

### 참고 : 큐 생성 방법 과 시간복잡도

1. collections.deque 사용
- append(item) : O(1)
- popleft() : O(1)

2. 리스트 사용 
- append(item) : O(1)
- pop(0) : O(n)

3. queue.Queue 사용 (멀티스레딩 환경에서, 병렬처리)
- put(item) : O(1)
- get() : O(1)
