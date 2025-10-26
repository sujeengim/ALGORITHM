<img width="554" height="292" alt="image" src="https://github.com/user-attachments/assets/0b238830-cceb-4d96-94de-2aa01d33459d" />

### DFS : 깊이 우선 탐색 
#### 한 방향으로 최대한 깊게 파고들어 탐색합니다. (재귀 사용)

```python
def dfs_recursive(graph, v, visited):
    visited[v] = True

    for neighbor in graph[v]: # 현재 노드와 연결된 노드들
        if not visited[neighbor]: #방문한 적 없으면 
            dfs_recursive(graph, neighbor, visited) #더 깊이 탐색

# 예시 그래프 
graph = [
    [],
    [2, 3],     
    [1, 7],     
    [1, 4, 5],
    [3, 6],
    [3, 7],
    [4, 8],
    [2, 5, 8],
    [6, 7]
]

visited_dfs = [False] * len(graph) # 방문한 곳 저장
dfs_recursive(graph, 1, visited_dfs)
# 예상 출력: 1 2 7 5 3 4 6 8
```
