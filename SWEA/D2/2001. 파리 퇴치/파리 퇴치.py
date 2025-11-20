
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    nbyn = []
    for i in range(n):
        nbyn.append(list(map(int, input().split())))

    max_sum = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            part_sum = 0
            for i in range(m):
                for j in range(m):
                    part_sum += nbyn[r+i][c+j]
            if part_sum > max_sum:
                max_sum = part_sum
    print(f"#{test_case} {max_sum}")
        
