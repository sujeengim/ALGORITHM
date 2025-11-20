T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nbyn = [[0]*n for _ in range(n)]

    dc = [1, 0, -1, 0] # 오왼 이동
    dr = [0, 1, 0, -1]  # 아래위 이동

    current_direction = 0 #현재 방향
    current_r, current_c = 0, 0 # 현재 좌표
    current_num = 1 # 현재 숫자

    while current_num <= n*n:
        nbyn[current_r][current_c] = current_num
        current_num += 1

        next_r = current_r + dr[current_direction]
        next_c = current_c + dc[current_direction]

        # 방향 바꾸기 
        if not(0<=next_r<=n-1 and 0<=next_c<=n-1) or nbyn[next_r][next_c] != 0:
            current_direction = (current_direction + 1) % 4
            next_r = current_r + dr[current_direction]
            next_c = current_c + dc[current_direction]

        current_r, current_c = next_r, next_c

    print(f"#{test_case}")
    for row in nbyn:
        print(*row)