from collections import deque

n, k = map(int, input().strip().split())
q = deque(range(1, n+1))
anslist = []

while len(q) > 1:
    q.rotate(-(k-1))
    anslist.append(q.popleft())
anslist.append(q.popleft())

print(f"<{', '.join(map(str, anslist))}>")