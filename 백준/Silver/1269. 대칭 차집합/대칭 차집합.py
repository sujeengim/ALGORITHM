n1, n2 = map(int, input().split())
n1list = set(map(int, input().split()))
n2list = set(map(int, input().split()))

intersection = n1list & n2list
ans = len(n1list) + len(n2list) - 2*len(intersection)
print(ans)