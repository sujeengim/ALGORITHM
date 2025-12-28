from collections import deque
import sys

N, K = map(int, sys.stdin.readline().strip().split())
deq = deque(range(1, N+1))
ans = []

for _ in range(N-1):
    for _ in range(K-1):
        deq.append(deq.popleft())
    ans.append(deq.popleft())
ans.append(deq.pop())

print("<" + ", ".join(map(str, ans)) + ">")