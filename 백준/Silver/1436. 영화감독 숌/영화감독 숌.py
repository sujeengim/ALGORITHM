
n = int(input())
if n == 1:
    print(666)
else:
    init = 666
    cnt = 1
    while True:
        if cnt == n:
            break
        init += 1
        if '666' in str(init):
            cnt += 1
        
    print(init) 
