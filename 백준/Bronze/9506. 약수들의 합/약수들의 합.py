while True:
    T = int(input())
    if T==-1:
        break
    Tlist = []
    for t in range(1, T):
        if T%t==0:
            Tlist.append(t)
    tsum = sum(Tlist)
    if tsum==T:
        
        print(T, '=', ' + '.join(list(map(str, Tlist))))
    else:
        print(T, 'is NOT perfect.')