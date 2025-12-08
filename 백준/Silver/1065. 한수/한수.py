import sys
N_str = sys.stdin.readline().strip()
N = int(N_str)

def is_hansu(n):
    n_str = str(n)
    L = len(n_str)
    
    if L <= 2:
        return True
    d = int(n_str[1]) - int(n_str[0])

    for i in range(1, L - 1): 
        current_diff = int(n_str[i+1]) - int(n_str[i])

        if current_diff != d:
            return False
    return True

if N < 100:
    ans = N
else:
    ans = 99
    
    for checknum in range(100, N + 1):
        if is_hansu(checknum):
            ans += 1

print(ans)