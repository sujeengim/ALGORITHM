n = int(input())
origin = list(map(int, input().split())) # 3 4 2
comp = sorted(list(set(origin))) # 2 3 4
comp_dic = {}
for i, v in enumerate(comp):
    comp_dic[v] = i
for v in origin:
    print(comp_dic[v], end=' ')