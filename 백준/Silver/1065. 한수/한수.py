import sys
N_str = sys.stdin.readline().strip()
N = int(N_str)

if N < 100:
    ans = N
else:
    ans = 99
    
    for checknum in range(100, N + 1):
        n_str = str(checknum)
        L = len(n_str)
        flag = 0
        d = int(n_str[1]) - int(n_str[0])

        for i in range(1, L - 1): 
            current_diff = int(n_str[i+1]) - int(n_str[i])
            if current_diff != d:
                flag = 1
                break

        if flag == 0:
            ans += 1

print(ans)
