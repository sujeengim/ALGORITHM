n, m = map(int, input().strip().split())
board = []
result = []

for _ in range(n):
    board.append(list(input()))

for i in range(n - 7):
    for j in range(m - 7):
        cnt_w = 0
        cnt_b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:  # 짝수 위치
                    if board[k][l] == 'W':
                        cnt_b += 1
                    else:
                        cnt_w += 1
                else:  # 홀수 위치
                    if board[k][l] == 'B':
                        cnt_b += 1
                    else:
                        cnt_w += 1
        result.append(cnt_b)
        result.append(cnt_w)

print(min(result))  